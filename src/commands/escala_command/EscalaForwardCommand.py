from commands.Command import Command


class EscalaForwardCommand(Command):

    def execute(self, sistema):
        sistema.repositorio_escala.nextMemento()
        memento = sistema.repositorio_escala.readEscala()
        text = ""
        text += "avançou uma escala"
        text += f"\n"
        sistema.tela.set_conteudo(text)
        sistema.tela.set_escala(memento)