from RelaorioTemplate import RelatorioTemplate
from RelatorioCSV import RelatorioCSV
from RelatorioDocX import RelatorioDocX

class RelatorioFactory:

    @staticmethod
    def generate_relatorio_padrao(tipo="csv") -> RelatorioTemplate:
        if tipo == "csv":
            return RelatorioCSV()
        elif tipo == "docx":
            return RelatorioDocX()
        else:
            raise ValueError(f"Tipo de relatório não suportado: {tipo}")
