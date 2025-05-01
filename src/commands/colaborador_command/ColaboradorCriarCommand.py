from commands.Command import Command
from persistencia.entidades.Colaborador import Colaborador


class ColaboradorCriarCommand(Command):
    def execute(self, sistema):
        print("criando colaborador")

        nome = input("nome: ")
        id = input("id: ")
        disciplinas = input("disciplinas (separadas por vírgula): ")
        turno = input("turnos (separados por vírgula): ")


        try:
            colaborador = Colaborador(
                nome,
                int(id),
                disciplinas.split(','),
                [t.strip() for t in turno.split(',')]
            )
            sistema.repositorio_colaborador.createColaborador(colaborador)
        except Exception as e:
            print(f"Erro ao criar colaborador: {e}")
            input("Pressione Enter para continuar...")