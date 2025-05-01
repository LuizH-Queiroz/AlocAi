from commands.escala_command.EscalaCommandFactory import EscalaCommandFactory
from commands.colaborador_command.ColaboradorCommandFactory import ColaboradorCommandFactory


class CommandFactory:
    def get_escala_command_factory(self):
        return EscalaCommandFactory()
    
    def get_colaborador_command_factory(self):
        return ColaboradorCommandFactory()