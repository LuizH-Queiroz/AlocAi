from commands.Command import Command


class ColaboradorDeletarCommand(Command):
    def execute(self, sistema):
        # self.tela = Memento next escala
        sistema.tela.set_conteudo("deletando colaborador")
        
        id = input("id do colaborador a ser editado: ")
        id = int(id)
        try:
            sistema.repositorio_colaborador.deleteColaborador(id)
            print(f"Colaborador de id {id} deletado com sucesso")
        except Exception as e:
            print("Falha em deletar colaborador")
            print(e)