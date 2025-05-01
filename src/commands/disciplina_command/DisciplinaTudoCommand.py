from commands.Command import Command


class DisciplinaTudoCommand(Command):
    def execute(self, sistema):
        print("mostrando todas as disciplinas")
 
        texto = ""
        disciplinas = sistema.repositorio_disciplina.readAllDisciplina()
        for disciplina in disciplinas:
            texto += f"ID: {disciplina.getId()}\n"
            texto += f"Nome: {disciplina.getNome()}\n"
            texto += "Turnos: "
            texto += " ".join(str(turno) for turno in disciplina.getTurnos())
            texto += "\n"
            texto += "-" * 30
            texto += "\n"
        sistema.tela.set_conteudo(texto)