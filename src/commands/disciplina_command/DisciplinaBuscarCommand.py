from commands.Command import Command


class DisciplinaBuscarCommand(Command):
    def execute(self, sistema):
        print("buscando disciplina")

        id = int(input("id da disciplina a ser editada: "))
        try:
            disciplina = sistema.repositorio_disciplina.readDisciplina(id)
            
            texto = ""

            texto += f"ID: {disciplina.getId()}\n"
            texto += f"Nome: {disciplina.getNome()}\n"
            texto += "Turnos: "
            texto += " ".join(str(turno) for turno in disciplina.getTurnos())
            texto += "\n"
            texto += "-" * 30

            sistema.tela.set_conteudo(texto)

        except Exception as e:
            sistema.tela.set_conteudo(e)
