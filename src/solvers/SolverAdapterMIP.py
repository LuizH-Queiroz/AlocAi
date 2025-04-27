from .SolverMIP import SolverMIP
from .Solver import Solver

class SolverAdapterMIP(Solver):

    def __init__(self, solver: SolverMIP):
        self._solver = solver
        self._data = None

    def solve(self):
        return self._solver.solve()
