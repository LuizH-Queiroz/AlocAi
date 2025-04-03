from abc import ABC, abstractmethod
from persistencia.DAOs.RAM_ColaboradorDAO import RAM_ColaboradorDAO
from persistencia.DAOs.RAM_EscalaDAO import RAM_EscalaDAO

class RelatorioTemplate(ABC):
    def gerar_relatorio(self):
        colaboradores = self._get_colaboradores(RAM_ColaboradorDAO())
        escala = self._get_escala_geral(RAM_EscalaDAO())
        self._imprime_relatorio(colaboradores, escala)

    @abstractmethod
    def _get_colaboradores(self, dao_colaboradores: RAM_ColaboradorDAO):
        pass

    @abstractmethod
    def _get_escala_geral(self, dao_escala: RAM_EscalaDAO):
        pass

    @abstractmethod
    def _imprime_relatorio(self, colaboradores, escala):
        pass
