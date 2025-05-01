from commands.Command import Command


class ColaboradorDeletarCommand(Command):
    def execute(self, sistema):
        # self.tela = Memento next escala
        
        id = input("id do colaborador a ser editado: ")
        try:
            id = int(id)
            sistema.repositorio_colaborador.deleteColaborador(id)
            sistema.tela.set_conteudo(f"Colaborador de id {id} deletado com sucesso")
        except Exception as e:
            sistema.tela.set_conteudo(f"Falha em deletar colaborador: {e}")