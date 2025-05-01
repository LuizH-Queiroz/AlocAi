from commands.Command import Command


class ColaboradorBuscarCommand(Command):
    def execute(self, sistema):
        # self.relatorio_template.gerar_relatorio()
        print("buscando colaborador")
        id = input("id do colaborador a ser encontrado: ")
        try:
            id = int(id)
            colaborador = sistema.repositorio_colaborador.readColaborador(id)
            
            texto = ""

            texto += f"ID: {colaborador.getId()}\n"
            texto += f"Nome: {colaborador.getNome()}\n"
            texto += "Turnos: "
            texto += ", ".join(str(turno) for turno in colaborador.getTurnos())
            texto += "\n"
            texto += "-" * 30

            sistema.tela.set_conteudo(texto)

        except Exception as e:
            sistema.tela.set_conteudo(e)