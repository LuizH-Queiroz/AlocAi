from commands.disciplina_command.DisciplinaBuscarCommand import DisciplinaBuscarCommand
from commands.disciplina_command.DisciplinaCriarCommand import DisciplinaCriarCommand
from commands.disciplina_command.DisciplinaDeletarCommand import DisciplinaDeletarCommand
from commands.disciplina_command.DisciplinaEditarCommand import DisciplinaEditarCommand
from commands.disciplina_command.DisciplinaTudoCommand import DisciplinaTudoCommand


class DisciplinaCommandFactory:
    def get_criar_command(self):
        return DisciplinaCriarCommand()

    def get_buscar_command(self):
        return DisciplinaBuscarCommand()

    def get_deletar_command(self):
        return DisciplinaDeletarCommand()

    def get_editar_command(self):
        return DisciplinaEditarCommand()

    def get_tudo_command(self):
        return DisciplinaTudoCommand()