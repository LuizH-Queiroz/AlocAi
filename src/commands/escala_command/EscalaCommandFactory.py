from commands.escala_command.EscalaBackCommand import EscalaBackCommand
from commands.escala_command.EscalaCreateCommand import EscalaCreateCommand
from commands.escala_command.EscalaForwardCommand import EscalaForwardCommand


class EscalaCommandFactory:

    def get_back_command(self):
        return EscalaBackCommand()

    def get_forward_command(self):
        return EscalaForwardCommand()

    def get_create_command(self):
        return EscalaCreateCommand()