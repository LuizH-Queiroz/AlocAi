from commands.Command import Command


class EscalaBackCommand(Command):

    def execute(self, sistema):
        sistema.repositorio_escala.previousMemento()
        memento = sistema.repositorio_escala.readEscala()
        text = ""
        text += "voltou uma escala"
        text += f"\n"
        sistema.tela.set_conteudo(text)
        sistema.tela.set_escala(memento)
