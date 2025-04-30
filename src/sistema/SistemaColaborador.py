from persistencia.entidades.Colaborador import Colaborador
from sistema.sistema import Sistema
from ui.UIFactory import UIFactory


class SistemaColaborador(Sistema):
    def __init__(self):
        self.tela = UIFactory().generateCCUI()
        super().__init__()

    def runSystem(self):
        self._show_tela()
        
        choice = input("")

        while(True):
            match choice.lower():
                case "criar":
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

                    self.repositorio_colaborador.createColaborador(colaborador)
                case "deletar":
                    # self.tela = Memento next escala
                    self.tela.set_conteudo("deletando colaborador")
                    
                    id = input("id do colaborador a ser editado: ")
                    id = int(id)
                    try:
                        self.repositorio_colaborador.deleteColaborador(id)
                        print(f"Colaborador de id {id} deletado com sucesso")
                    except Exception as e:
                        print("Falha em deletar colaborador")
                        print(e)

                case "buscar":
                    # self.relatorio_template.gerar_relatorio()
                    print("buscando colaborador")
                    id = input("id do colaborador a ser encontrado: ")
                    id = int(id)
                    try:
                        colaborador = self.repositorio_colaborador.readColaborador(id)
                        
                        texto = ""

                        texto += f"ID: {colaborador.getId()}\n"
                        texto += f"Nome: {colaborador.getNome()}\n"
                        texto += "Turnos: "
                        texto += ", ".join(str(turno) for turno in colaborador.getTurnos())
                        texto += "\n"
                        texto += "-" * 30

                        self.tela.set_conteudo(texto)

                    except Exception as e:
                        self.tela.set_conteudo(e)
          
                case "tudo":
                    # self.relatorio_template.gerar_relatorio()
                    texto = ""
                    texto += "mostrando todos os colaboradores\n"
                    colaboradores = self.repositorio_colaborador.readAllColaborador()
                    for colaborador in colaboradores:
                        texto += f"ID: {colaborador.getId()}\n"
                        texto += f"Nome: {colaborador.getNome()}\n"
                        texto += "Turnos: "
                        texto += ", ".join(str(turno) for turno in colaborador.getTurnos())
                        texto += "\n"
                        texto += "-" * 30
                        texto += "\n"
                    self.tela.set_conteudo(texto)
                case "editar":
                    # self.relatorio_template.gerar_relatorio()
                    self.tela.set_conteudo("editando colaborador")
                    id = input("id do colaborador a ser editado: ")
                    id = int(id)
                    try:
                        colaborador = self.repositorio_colaborador.readColaborador(id)

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
                                self.repositorio_colaborador.updateColaborador(
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
                                self.repositorio_colaborador.updateColaborador(
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
                                self.repositorio_colaborador.updateColaborador(
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
                                self.repositorio_colaborador.updateColaborador(
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

                case "main":
                    self.tela = UIFactory().generateMainUI()
                case _:
                    self.tela.set_conteudo("opção não existe!")
            
            self.tela.show()

            if choice == "main":
                return
            
            choice = input("")
