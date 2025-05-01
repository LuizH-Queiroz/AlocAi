from persistencia.entidades.Escala import Escala
from sistema.sistema import Sistema
from commands.CommandFactory import CommandFactory
from ui.UIFactory import UIFactory


class SistemaEscala(Sistema):
    def __init__(self):
        self.tela = UIFactory().generateEscalaUI()
        self.command_factory = CommandFactory().get_sistema_command_factory()
        super().__init__()

    def runSystem(self):
        self.tela.set_escala(self.repositorio_escala.readEscala())
        self._show_tela()

        choice = input("")

        while(True):
            self.command = None

            match choice.lower():
                case "back":
                    self.command = self.command_factory.get_back_command()

                case "forward":
                    self.command = self.command_factory.get_forward_command()

                case "create":
                    self.command = self.command_factory.get_create_command()

                case "main":
                    self.tela = UIFactory().generateMainUI()
                    
                case _:
                    self.tela.set_conteudo("opção não existe!")
                    self.tela.set_escala(self.repositorio_escala.readEscala())
                
            if self.command:
                self.command.execute(self)
            
            self._show_tela()

            if choice == "main":
                return
            
            choice = input("")
