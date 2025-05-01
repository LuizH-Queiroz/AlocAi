import subprocess
from .Solver import Solver
from .School_timetabling_main.main_code.data import Data
from .School_timetabling_main.main_code.formulacao_MIP import Formulacao
from .School_timetabling_main.main_code.write_solution import Write_solution

class SolverMIP(Solver):

    def solve(self):
        data = Data()
        data.load()
        # data.get_fixed_vars()

        formulacao = Formulacao(data)
        # status = formulacao.relax_and_fix()

        formulacao.create_model()
        status = formulacao.solve_model()

        if status:
            solution = Write_solution(data)
            solution.write_excel_professor()
            solution.write_excel_dia_slot()

            return formulacao.print_solution() 
        else:
            return 'Solução viável não encontrada.'