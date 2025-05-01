from commands.colaborador_command.ColaboradorBuscarCommand import ColaboradorBuscarCommand
from commands.colaborador_command.ColaboradorCriarCommand import ColaboradorCriarCommand
from commands.colaborador_command.ColaboradorDeletarCommand import ColaboradorDeletarCommand
from commands.colaborador_command.ColaboradorEditarCommand import ColaboradorEditarCommand
from commands.colaborador_command.ColaboradorTudoCommand import ColaboradorTudoCommand


class ColaboradorCommandFactory:
    def get_criar_command(self): 
        return ColaboradorCriarCommand()

    def get_deletar_command(self):
        return ColaboradorDeletarCommand()

    def get_editar_command(self):
        return ColaboradorEditarCommand()

    def get_tudo_command(self):
        return ColaboradorTudoCommand()

    def get_buscar_command(self):
        return ColaboradorBuscarCommand()