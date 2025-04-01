from .Solver import Solver
from .SolverMIP import SolverMIP
from .SolverAdapterMIP import SolverAdapterMIP

class AdapterFactory:

    @staticmethod
    def generateSolverAdapterMIP():
        return SolverAdapterMIP(SolverMIP())