from abc import ABC, abstractmethod
from persistencia.interfaces import ColaboradorDAO, EscalaDAO

class RelatorioTemplate(ABC):
    def gerar_relatorio(self, colaboradorDAO, escalaDAO):
        colaboradores = self._get_colaboradores(colaboradorDAO)
        escala = self._get_escala_geral(escalaDAO)
        self._imprime_relatorio(colaboradores, escala)

    @abstractmethod
    def _get_colaboradores(self, dao_colaboradores: ColaboradorDAO):
        pass

    @abstractmethod
    def _get_escala_geral(self, dao_escala: EscalaDAO):
        pass

    @abstractmethod
    def _imprime_relatorio(self, colaboradores, escala):
        pass
