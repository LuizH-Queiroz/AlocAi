from commands.Command import Command


class ColaboradorTudoCommand(Command):
    def execute(self, sistema):

        try:
            # self.relatorio_template.gerar_relatorio()
            texto = ""
            texto += "mostrando todos os colaboradores\n"
            colaboradores = sistema.repositorio_colaborador.readAllColaborador()
            for colaborador in colaboradores:
                texto += f"ID: {colaborador.getId()}\n"
                texto += f"Nome: {colaborador.getNome()}\n"
                texto += "Turnos: "
                texto += ", ".join(str(turno) for turno in colaborador.getTurnos())
                texto += "\n"
                texto += "-" * 30
                texto += "\n"
            sistema.tela.set_conteudo(texto)
        except Exception as e:
            print(f"Falha em mostrar todos os colaboradores: {e}")
            sistema.tela.set_conteudo(f"Falha em mostrar todos os colaboradores: {e}")