from sistema.sistema import Sistema
from commands.CommandFactory import CommandFactory
from ui.UIFactory import UIFactory


class SistemaDisciplina(Sistema):
    def __init__(self):
        self.tela = UIFactory().generateDisciplinaUI()
        self.command_factory = CommandFactory().get_disciplina_command_factory()
        super().__init__()

    def runSystem(self):
        self._show_tela()
        
        choice = input("")

        while(True):
            self.command = None

            match choice.lower():
                case "criar":
                    self.command = self.command_factory.get_criar_command()

                case "deletar":
                    self.command = self.command_factory.get_deletar_command()

                case "buscar":
                    self.command = self.command_factory.get_buscar_command()

                case "tudo":
                    self.command = self.command_factory.get_tudo_command()

                case "editar":
                    self.command = self.command_factory.get_editar_command()

                case "main":
                    self.tela = UIFactory().generateMainUI()

                case _:
                    self.tela.set_conteudo("opção não existe!")

            if self.command:
                self.command.execute(self)
        
            self.tela.show()

            if choice == "main":
                return
            
            choice = input("")