from .SolverMIP import SolverMIP
from .Solver import Solver

class SolverAdapterMIP(Solver):

    def __init__(self, solver: SolverMIP):
        self._solver = solver
        self._data = None
    
    def converteDados(self, data):
        self._data = data
        return f"retornando novo data + {self._data}"

    def solve(self):
        return self._solver.solve()
