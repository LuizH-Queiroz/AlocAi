from .RelatorioCSV import RelatorioCSV
from .RelatorioDocX import RelatorioDocX

class RelatorioFactory:

    @staticmethod
    def generate_relatorio_CSV():
        return RelatorioCSV()
    
    @staticmethod
    def generate_relatorio_DOCX():
        return RelatorioDocX()
