from commands.Command import Command


class DisciplinaDeletarCommand(Command):
    def execute(self, sistema):
        print("deletando disciplina")
                    
        id = int(input("id da disciplina a ser editada: "))
        try:
            sistema.repositorio_disciplina.deleteDisciplina(id)
            print(f"Disciplina de id {id} deletada com sucesso")
        except Exception as e:
            print("Falha em deletar disciplina")
            print(e)