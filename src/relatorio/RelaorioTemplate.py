from abc import ABC, abstractmethod

class RelatorioTemplate(ABC):
    def gerar_relatorio(self):
        colaboradores = self.get_colaboradores()
        escala = self.get_escala_geral()
        self.imprime_relatorio(colaboradores, escala)

    @abstractmethod
    def get_colaboradores(self):
        pass

    @abstractmethod
    def get_escala_geral(self):
        pass

    @abstractmethod
    def imprime_relatorio(self, colaboradores, escala):
        pass
