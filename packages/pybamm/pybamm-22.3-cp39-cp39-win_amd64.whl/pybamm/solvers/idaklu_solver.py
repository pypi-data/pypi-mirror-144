#
# Solver class using sundials with the KLU sparse linear solver
#
import casadi
import pybamm
import numpy as np
import scipy.sparse as sparse

import importlib

idaklu_spec = importlib.util.find_spec("pybamm.solvers.idaklu")
if idaklu_spec is not None:
    try:
        idaklu = importlib.util.module_from_spec(idaklu_spec)
        idaklu_spec.loader.exec_module(idaklu)
    except ImportError:  # pragma: no cover
        idaklu_spec = None


def have_idaklu():
    return idaklu_spec is not None


class IDAKLUSolver(pybamm.BaseSolver):
    """Solve a discretised model, using sundials with the KLU sparse linear solver.

     Parameters
    ----------
    rtol : float, optional
        The relative tolerance for the solver (default is 1e-6).
    atol : float, optional
        The absolute tolerance for the solver (default is 1e-6).
    root_method : str or pybamm algebraic solver class, optional
        The method to use to find initial conditions (for DAE solvers).
        If a solver class, must be an algebraic solver class.
        If "casadi",
        the solver uses casadi's Newton rootfinding algorithm to find initial
        conditions. Otherwise, the solver uses 'scipy.optimize.root' with method
        specified by 'root_method' (e.g. "lm", "hybr", ...)
    root_tol : float, optional
        The tolerance for the initial-condition solver (default is 1e-6).
    extrap_tol : float, optional
        The tolerance to assert whether extrapolation occurs or not (default is 0).
    """

    def __init__(
        self,
        rtol=1e-6,
        atol=1e-6,
        root_method="casadi",
        root_tol=1e-6,
        extrap_tol=0,
        max_steps="deprecated",
    ):

        if idaklu_spec is None:  # pragma: no cover
            raise ImportError("KLU is not installed")

        super().__init__(
            "ida",
            rtol,
            atol,
            root_method,
            root_tol,
            extrap_tol,
            max_steps,
        )
        self.name = "IDA KLU solver"

        pybamm.citations.register("Hindmarsh2000")
        pybamm.citations.register("Hindmarsh2005")

    def set_atol_by_variable(self, variables_with_tols, model):
        """
        A method to set the absolute tolerances in the solver by state variable.
        This method attaches a vector of tolerance to the model. (i.e. model.atol)

        Parameters
        ----------
        variables_with_tols : dict
            A dictionary with keys that are strings indicating the variable you
            wish to set the tolerance of and values that are the tolerances.

        model : :class:`pybamm.BaseModel`
            The model that is going to be solved.
        """

        size = model.concatenated_initial_conditions.size
        atol = self._check_atol_type(self.atol, size)
        for var, tol in variables_with_tols.items():
            variable = model.variables[var]
            if isinstance(variable, pybamm.StateVector):
                atol = self.set_state_vec_tol(atol, variable, tol)
            else:
                raise pybamm.SolverError("Can only set tolerances for state variables")

        model.atol = atol

    def set_state_vec_tol(self, atol, state_vec, tol):
        """
        A method to set the tolerances in the atol vector of a specific
        state variable. This method modifies self.atol

        Parameters
        ----------
        state_vec : :class:`pybamm.StateVector`
            The state vector to apply to the tolerance to
        tol: float
            The tolerance value
        """
        slices = state_vec.y_slices[0]
        atol[slices] = tol
        return atol

    def _check_atol_type(self, atol, size):
        """
        This method checks that the atol vector is of the right shape and
        type.

        Parameters
        ----------
        atol: double or np.array or list
            Absolute tolerances. If this is a vector then each entry corresponds to
            the absolute tolerance of one entry in the state vector.
        size: int
            The length of the atol vector
        """

        if isinstance(atol, float):
            atol = atol * np.ones(size)
        elif isinstance(atol, list):
            atol = np.array(atol)
        elif isinstance(atol, np.ndarray):
            pass
        else:
            raise pybamm.SolverError(
                "Absolute tolerances must be a numpy array, float, or list"
            )

        if atol.size != size:
            raise pybamm.SolverError(
                """Absolute tolerances must be either a scalar or a numpy arrray
                of the same shape as y0 ({})""".format(
                    size
                )
            )

        return atol

    def _integrate(self, model, t_eval, inputs_dict=None):
        """
        Solve a DAE model defined by residuals with initial conditions y0.

        Parameters
        ----------
        model : :class:`pybamm.BaseModel`
            The model whose solution to calculate.
        t_eval : numeric type
            The times at which to compute the solution
        inputs_dict : dict, optional
            Any external variables or input parameters to pass to the model when solving
        """
        inputs_dict = inputs_dict or {}
        if model.convert_to_format == "casadi":
            # stack inputs
            inputs = casadi.vertcat(*[x for x in inputs_dict.values()])
            # raise warning about casadi format being slow
            pybamm.logger.warning(
                "Using casadi form for the IDA KLU solver is slow. "
                "Set `model.convert_to_format='python'` for better performance. "
                "For DAE models, this may also require changing the root method to "
                "'lm'."
            )
        else:
            inputs = inputs_dict

        if model.jac_rhs_algebraic_eval is None:
            raise pybamm.SolverError("KLU requires the Jacobian to be provided")

        try:
            atol = model.atol
        except AttributeError:
            atol = self.atol

        y0 = model.y0
        if isinstance(y0, casadi.DM):
            y0 = y0.full()
        y0 = y0.flatten()

        rtol = self.rtol
        atol = self._check_atol_type(atol, y0.size)

        if model.convert_to_format == "jax":
            mass_matrix = model.mass_matrix.entries.toarray()
        else:
            mass_matrix = model.mass_matrix.entries

        # construct residuals function by binding inputs
        if model.convert_to_format == "casadi":
            def resfn(t, y, ydot):
                return (
                    model.rhs_algebraic_eval(t, y, inputs).full().flatten()
                    - mass_matrix @ ydot
                )
        else:
            def resfn(t, y, ydot):
                return (
                    model.rhs_algebraic_eval(t, y, inputs).flatten()
                    - mass_matrix @ ydot
                )

        jac_y0_t0 = model.jac_rhs_algebraic_eval(t_eval[0], y0, inputs)
        if sparse.issparse(jac_y0_t0):
            def jacfn(t, y, cj):
                j = model.jac_rhs_algebraic_eval(t, y, inputs) - cj * mass_matrix
                return j
        else:
            def jacfn(t, y, cj):
                jac_eval = model.jac_rhs_algebraic_eval(t, y, inputs) - cj * mass_matrix
                return sparse.csr_matrix(jac_eval)

        class SundialsJacobian:
            def __init__(self):
                self.J = None

                random = np.random.random(size=y0.size)
                J = jacfn(10, random, 20)
                self.nnz = J.nnz  # hoping nnz remains constant...

            def jac_res(self, t, y, cj):
                # must be of form j_res = (dr/dy) - (cj) (dr/dy')
                # cj is just the input parameter
                # see p68 of the ida_guide.pdf for more details
                self.J = jacfn(t, y, cj)

            def get_jac_data(self):
                return self.J.data

            def get_jac_row_vals(self):
                return self.J.indices

            def get_jac_col_ptrs(self):
                return self.J.indptr

        # solver works with ydot0 set to zero
        ydot0 = np.zeros_like(y0)

        jac_class = SundialsJacobian()

        num_of_events = len(model.terminate_events_eval)
        use_jac = 1

        def rootfn(t, y):
            return_root = np.ones((num_of_events,))
            return_root[:] = [
                event(t, y, inputs) for event in model.terminate_events_eval
            ]

            return return_root

        # get ids of rhs and algebraic variables
        rhs_ids = np.ones(model.rhs_eval(0, y0, inputs).shape[0])
        alg_ids = np.zeros(len(y0) - len(rhs_ids))
        ids = np.concatenate((rhs_ids, alg_ids))

        number_of_sensitivity_parameters = 0
        if model.jacp_rhs_algebraic_eval is not None:
            sens0 = model.jacp_rhs_algebraic_eval(0, y0, inputs)
            number_of_sensitivity_parameters = len(sens0.keys())

        def sensfn(resvalS, t, y, yp, yS, ypS):
            """
            this function evaluates the sensitivity equations required by IDAS,
            returning them in resvalS, which is preallocated as a numpy array of size
            (np, n), where n is the number of states and np is the number of parameters

            The equations returned are:

             dF/dy * s_i + dF/dyd * sd_i + dFdp_i for i in range(np)

            Parameters
            ----------
            resvalS: ndarray of shape (np, n)
                returns the sensitivity equations in this preallocated array
            t: number
                time value
            y: ndarray of shape (n)
                current state vector
            yp: list (np) of ndarray of shape (n)
                current time derivative of state vector
            yS: list (np) of ndarray of shape (n)
                current state vector of sensitivity equations
            ypS: list (np) of ndarray of shape (n)
                current time derivative of state vector of sensitivity equations

            """

            dFdy = model.jac_rhs_algebraic_eval(t, y, inputs)
            dFdyd = mass_matrix
            dFdp = model.jacp_rhs_algebraic_eval(t, y, inputs)

            for i, dFdp_i in enumerate(dFdp.values()):
                resvalS[i][:] = dFdy @ yS[i] - dFdyd @ ypS[i] + dFdp_i

        # solve
        timer = pybamm.Timer()
        sol = idaklu.solve(
            t_eval,
            y0,
            ydot0,
            resfn,
            jac_class.jac_res,
            sensfn,
            jac_class.get_jac_data,
            jac_class.get_jac_row_vals,
            jac_class.get_jac_col_ptrs,
            jac_class.nnz,
            rootfn,
            num_of_events,
            use_jac,
            ids,
            atol,
            rtol,
            number_of_sensitivity_parameters,
        )
        integration_time = timer.time()

        t = sol.t
        number_of_timesteps = t.size
        number_of_states = y0.size
        y_out = sol.y.reshape((number_of_timesteps, number_of_states))

        # return sensitivity solution, we need to flatten yS to
        # (#timesteps * #states,) to match format used by Solution
        if number_of_sensitivity_parameters != 0:
            yS_out = {
                name: sol.yS[i].reshape(-1, 1) for i, name in enumerate(sens0.keys())
            }
        else:
            yS_out = False
        if sol.flag in [0, 2]:
            # 0 = solved for all t_eval
            if sol.flag == 0:
                termination = "final time"
            # 2 = found root(s)
            elif sol.flag == 2:
                termination = "event"

            sol = pybamm.Solution(
                sol.t,
                np.transpose(y_out),
                model,
                inputs_dict,
                t[-1],
                np.transpose(y_out[-1])[:, np.newaxis],
                termination,
                sensitivities=yS_out,
            )
            sol.integration_time = integration_time
            return sol
        else:
            raise pybamm.SolverError(sol.message)
