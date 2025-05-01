from abc import ABC, abstractmethod

from persistencia.persistenciaFactories.PersistenciaFactory import PersistenciaFactory
from relatorio.RelatorioFactory import RelatorioFactory
from solvers.AdapterFactory import AdapterFactory


class Sistema(ABC):

    def __init__(self):
        self.repositorio_colaborador = PersistenciaFactory().getColaboradorRepository()
        self.relatorio_template = RelatorioFactory().generate_relatorio_CSV()
        self.repositorio_escala = PersistenciaFactory().getEscalaRepository()
        self.repositorio_disciplina = PersistenciaFactory().getDisciplinaRepository()
        self.solver_adapter = AdapterFactory().generateSolverAdapterMIP()
            
    @abstractmethod
    def runSystem(self):
        pass

    def _show_tela(self):
        self.tela.show()