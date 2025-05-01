from commands.Command import Command
from persistencia.entidades.Disciplina import Disciplina


class DisciplinaEditarCommand(Command):
    def execute(self, sistema):
        print("editando disciplina")

        id = input("id da disciplina a ser editada: ")
        try:
            
            disciplina = self.repositorio_disciplina.readDisciplina(int(id))

            if disciplina:
                print(f"ID: {disciplina.getId()}")
                print(f"Nome: {disciplina.getNome()}")
                print("Turnos:", end=" ")
                print(" ".join(str(turno) for turno in disciplina.getTurnos()))
                print("-" * 30)

                print(disciplina)
                print(type(disciplina))

                campo = input("campo a ser editado (nome, id, Turnos): ")
                if campo == "nome":
                    novo_nome = input("novo nome: ")
                    self.repositorio_disciplina.updateDisciplina(
                        id,
                        Disciplina(
                            novo_nome,
                            disciplina.getId(),
                            disciplina.getTurnos()
                        )
                    )
                elif campo == "id":
                    novo_id = int(input("novo id: "))
                    disciplina.setId(novo_id)
                    self.repositorio_disciplina.updateDisciplina(
                        id,
                        Disciplina(
                            disciplina.getNome(),
                            novo_id,
                            disciplina.getTurnos()
                            )
                    )
                elif campo == "Turnos":
                    novos_Turnos = input("novos Turnos: ")
                    novos_Turnos = novos_Turnos.split()
                    disciplina.setTurnos(novos_Turnos)
                    self.repositorio_disciplina.updateDisciplina(
                        id,
                        Disciplina(
                            disciplina.getNome(),
                            disciplina.getId(),
                            novos_Turnos
                            )
                    )
                else:
                    print("campo inválido")
        except Exception as e:
            print(e)
        
        input("Aperte qualquer tecla para retornar ao menu")