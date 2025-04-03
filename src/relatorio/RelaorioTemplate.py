from abc import ABC, abstractmethod
from persistencia.DAOs.RAM_ColaboradorDAO import RAM_ColaboradorDAO
from persistencia.DAOs.RAM_EscalaDAO import RAM_EscalaDAO

class RelatorioTemplate(ABC):
    def gerar_relatorio(self):
        colaboradores = self.get_colaboradores()
        escala = self.get_escala_geral()
        self.imprime_relatorio(colaboradores, escala)

    def get_colaboradores(self, dao_colaboradores: RAM_ColaboradorDAO):
        return dao_colaboradores.readAll()

    def get_escala_geral(self, dao_escala: RAM_EscalaDAO):
        return dao_escala.read()

    @abstractmethod
    def imprime_relatorio(self, colaboradores, escala):
        pass
