from commands.Command import Command
from persistencia.entidades.Colaborador import Colaborador


class ColaboradorEditarCommand(Command):
    def execute(self, sistema):
        # self.relatorio_template.gerar_relatorio()
        sistema.tela.set_conteudo("editando colaborador")
        id = input("id do colaborador a ser editado: ")
        id = int(id)
        try:
            colaborador = sistema.repositorio_colaborador.readColaborador(id)

            if colaborador:
                print(f"ID: {colaborador.getId()}")
                print(f"Nome: {colaborador.getNome()}")
                print("Disciplinas:", end=" ")
                print(", ".join(colaborador.getDisciplinas()))
                print("Turnos:", end=" ")
                print(", ".join(str(turno) for turno in colaborador.getTurnos()))
                print("-" * 30)

                campo = input("campo a ser editado (nome, id, disciplinas, turnos): ")
                
                if campo == "nome":
                    novo_nome = input("novo nome: ")
                    sistema.repositorio_colaborador.updateColaborador(
                        id,
                        Colaborador(
                            novo_nome,
                            colaborador.getId(),
                            colaborador.getDisciplinas(),
                            colaborador.getTurnos()
                        )
                    )
                
                elif campo == "id":
                    novo_id = int(input("novo id: "))
                    sistema.repositorio_colaborador.updateColaborador(
                        id,
                        Colaborador(
                            colaborador.getNome(),
                            novo_id,
                            colaborador.getDisciplinas(),
                            colaborador.getTurnos()
                        )
                    )
                
                elif campo == "disciplinas":
                    novas_disciplinas = input("novas disciplinas (separadas por vírgula): ")
                    novas_disciplinas = novas_disciplinas.split(',')
                    sistema.repositorio_colaborador.updateColaborador(
                        id,
                        Colaborador(
                            colaborador.getNome(),
                            colaborador.getId(),
                            novas_disciplinas,
                            colaborador.getTurnos()
                        )
                    )
                
                elif campo == "turnos":
                    novos_turnos = input("novos turnos (separados por vírgula): ")
                    novos_turnos = novos_turnos.split(',')
                    sistema.repositorio_colaborador.updateColaborador(
                        id,
                        Colaborador(
                            colaborador.getNome(),
                            colaborador.getId(),
                            colaborador.getDisciplinas(),
                            novos_turnos
                        )
                    )
                
                else:
                    print("campo inválido")

        except Exception as e:
            print(e)

        input("Aperte qualquer tecla para retornar ao menu")
