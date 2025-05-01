from commands.escala_command.EscalaCommandFactory import EscalaCommandFactory


class CommandFactory:
    def get_sistema_command_factory(self):
        return EscalaCommandFactory()