from RelaorioTemplate import RelatorioTemplate

class RelatorioDocX(RelatorioTemplate):
    def get_colaboradores(self):
        # PEGA COLABORADORES
        colaboradores = ["Carlos", "Fernanda", "Lucia"]
        return colaboradores

    def get_escala_geral(self):
        # PEGA A ESCALA
        escala = {"Carlos": "Turno A", "Fernanda": "Turno B", "Lucia": "Turno C"}
        return escala

    def imprime_relatorio(self, colaboradores, escala):
        print("Gerando relatório DOCX...")
        for colaborador in colaboradores:
            print(f"{colaborador}: {escala[colaborador]}")
