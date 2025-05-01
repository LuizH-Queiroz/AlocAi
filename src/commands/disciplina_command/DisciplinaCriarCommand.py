from commands.Command import Command
from persistencia.entidades.Disciplina import Disciplina


class DisciplinaCriarCommand(Command):
    def execute(self, sistema):
        print("criando disciplina")

        nome = input("nome: ")
        id = int(input("id: "))
        turnos = input("Turnos: ")

        disciplina = Disciplina(nome, id, [t.strip() for t in turnos.split(',')])
        sistema.repositorio_disciplina.createDisciplina(disciplina)