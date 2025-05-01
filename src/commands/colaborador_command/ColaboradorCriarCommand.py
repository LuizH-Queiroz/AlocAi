from commands.Command import Command
from persistencia.entidades.Colaborador import Colaborador


class ColaboradorCriarCommand(Command):
    def execute(self, sistema):
        print("criando colaborador")

        nome = input("nome: ")
        id = int(input("id: "))
        disciplinas = input("disciplinas (separadas por vírgula): ")
        turno = input("turnos (separados por vírgula): ")

        colaborador = Colaborador(
            nome,
            id,
            disciplinas.split(','),
            [t.strip() for t in turno.split(',')]
        )

        sistema.repositorio_colaborador.createColaborador(colaborador)