from persistencia.entidades.Disciplina import Disciplina
from sistema.sistema import Sistema
from ui.UIFactory import UIFactory


class SistemaDisciplina(Sistema):
    def __init__(self):
        self.tela = UIFactory().generateDisciplinaUI()
        super().__init__()

    def runSystem(self):
        self._show_tela()
        
        choice = input("")

        while(True):
            match choice.lower():
                case "criar":
                    print("criando disciplina")

                    nome = input("nome: ")
                    id = int(input("id: "))
                    turnos = input("Turnos: ")

                    disciplina = Disciplina(nome, id, [t.strip() for t in turnos.split(',')])
                    self.repositorio_disciplina.createDisciplina(disciplina)

                case "deletar":
                    print("deletando disciplina")
                    
                    id = int(input("id da disciplina a ser editada: "))
                    try:
                        self.repositorio_disciplina.deleteDisciplina(id)
                        print(f"Disciplina de id {id} deletada com sucesso")
                    except Exception as e:
                        print("Falha em deletar disciplina")
                        print(e)

                case "buscar":
                    print("buscando disciplina")

                    id = int(input("id da disciplina a ser editada: "))
                    try:
                        disciplina = self.repositorio_disciplina.readDisciplina(id)
                        
                        texto = ""

                        texto += f"ID: {disciplina.getId()}\n"
                        texto += f"Nome: {disciplina.getNome()}\n"
                        texto += "Turnos: "
                        texto += " ".join(str(turno) for turno in disciplina.getTurnos())
                        texto += "\n"
                        texto += "-" * 30

                        self.tela.set_conteudo(texto)

                    except Exception as e:
                        self.tela.set_conteudo(e)

                case "tudo":
                    print("mostrando todas as disciplinas")
 
                    texto = ""
                    disciplinas = self.repositorio_disciplina.readAllDisciplina()
                    for disciplina in disciplinas:
                        texto += f"ID: {disciplina.getId()}\n"
                        texto += f"Nome: {disciplina.getNome()}\n"
                        texto += "Turnos: "
                        texto += " ".join(str(turno) for turno in disciplina.getTurnos())
                        texto += "\n"
                        texto += "-" * 30
                        texto += "\n"
                    self.tela.set_conteudo(texto)

                case "editar":
                    print("editando disciplina")

                    id = int(input("id da disciplina a ser editada: "))
                    id = int(id)
                    try:
                        pass
                        disciplina = self.repositorio_disciplina.readDisciplina(id)

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

                case "main":
                    self.tela = UIFactory().generateMainUI()

                case _:
                    self.tela.set_conteudo("opção não existe!")
        
            self.tela.show()

            if choice == "main":
                return
            
            choice = input("")