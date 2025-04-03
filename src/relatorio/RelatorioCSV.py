from .RelaorioTemplate import RelatorioTemplate

class RelatorioCSV(RelatorioTemplate):

    def _get_colaboradores(self, dao_colaboradores):
        return dao_colaboradores.readAll()
    
    def _get_escala_geral(self, dao_escala):
        return dao_escala.read()

    def _imprime_relatorio(self, colaboradores, escala):
        print("CSV")
        print(colaboradores)
        print(escala)
