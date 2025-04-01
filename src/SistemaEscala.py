from solvers.Solver import Solver
from solvers.AdapterFactory import AdapterFactory

myAdapter = AdapterFactory.generateSolverAdapterMIP()
print(myAdapter.converteDados([1, 2, 3, 4, 5, 6]))
print(myAdapter.solve())