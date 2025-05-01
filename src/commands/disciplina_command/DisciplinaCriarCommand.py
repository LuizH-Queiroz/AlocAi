from commands.Command import Command
from persistencia.entidades.Disciplina import Disciplina


class DisciplinaCriarCommand(Command):
    def execute(self, sistema):
        print("criando disciplina")

        nome = input("nome: ")
        id = input("id: ")
        turnos = input("Turnos: ")

        try:
            disciplina = Disciplina(nome, int(id), [t.strip() for t in turnos.split(',')])
            sistema.repositorio_disciplina.createDisciplina(disciplina)
        except Exception as e:
            print(f"Erro ao criar disciplina: {e}")
            input("Pressione Enter para continuar...")