from persistencia.persistenciaFactories.PersistenciaFactory import PersistenciaFactory
from relatorio.RelatorioFactory import RelatorioFactory
from solvers.AdapterFactory import AdapterFactory
from persistencia.DAOs.CSV_ColaboradorDAO import CSV_ColaboradorDAO
from persistencia.DAOs.CSV_EscalaDAO import CSV_EscalaDAO
from persistencia.DAOs.CSV_DisciplinaDAO import CSV_DisciplinaDAO
from ui.UIFactory import UIFactory
from persistencia.entidades.Colaborador import Colaborador  
from persistencia.entidades.Disciplina import Disciplina
from persistencia.entidades.Escala import Escala
from abc import abstractmethod, ABC

class SistemaEscala:
    
    def __init__(self):        
        self.repositorio_colaborador = PersistenciaFactory().getColaboradorRepository()
        self.relatorio_template = RelatorioFactory().generate_relatorio_CSV()
        self.repositorio_escala = PersistenciaFactory().getEscalaRepository()
        self.repositorio_disciplina = PersistenciaFactory().getDisciplinaRepository()
        self.solver_adapter = AdapterFactory().generateSolverAdapterMIP()
        self.command = None
        self.tela = None

    def runSystem(self):
        self.tela = UIFactory().generateMainUI()
        self.tela.show()

        while(True):
            choice = input()
            match choice.lower():
                case '1':
                    self.tela = UIFactory().generateEscalaUI()
                    self.tela.set_escala(self.repositorio_escala.readEscala())
                    # self.command = SistemaEscala.EscalaCommand()
                case '2':
                    self.tela = UIFactory().generateCCUI()
                    # self.command = SistemaEscala.ColaboradorCommand()
                case '3':
                    self.tela = UIFactory().generateDisciplinaUI()
                    # self.command = SistemaEscala.Relaself.command = SistemaEscala.ColaboradorCommand()torioCommand()
                case '4':
                    self.tela = UIFactory().generateRelatorioUI()
                    # self.command = SistemaEscala.Relaself.command = SistemaEscala.ColaboradorCommand()torioCommand()
                case '0':
                    print('Saindo do sistema...')
                case _:
                    self.tela = UIFactory().generateMainUI()
                    self.tela.set_conteudo("Opção inválida! Tente novamente.")
                    self.tela.show()
                    continue
            
            if choice == '0':
                break
            
            # Interface específica
            self.tela.show()

            match choice.lower():
                case '1':
                    self._escalaSystem()
                case '2':
                    self._colaboradorSystem()
                case '3':
                    self._disciplinaSystem()
                case '4':
                    self._relatorioSystem()
                case _:
                    continue

    def _escalaSystem(self):
        choice = input("")

        while(True):
            match choice.lower():
                case "back":
                    self.repositorio_escala.previousMemento()
                    memento = self.repositorio_escala.readEscala()
                    text = ""
                    text += "voltou uma escala"
                    text += f"\n"
                    self.tela.set_conteudo(text)
                    self.tela.set_escala(memento)

                case "forward":
                    self.repositorio_escala.nextMemento()
                    memento = self.repositorio_escala.readEscala()
                    text = ""
                    text += "avançou uma escala"
                    text += f"\n"
                    self.tela.set_conteudo(text)
                    self.tela.set_escala(memento)

                case "create":
                    escala_str = self.solver_adapter.solve()  # isso retorna a string como a que você mandou

                    # Parse da string para gerar a lista de atribuições
                    atribuicoes = []
                    for linha in escala_str.strip().split("\n"):
                        if "→" in linha:
                            nome_disc, info = linha.split("→")
                            nome = nome_disc.strip()
                            disciplina, horario_str = info.strip().split("|")
                            disciplina = disciplina.strip()
                            dia_semana, slot_str = horario_str.strip().split(" - ")
                            slot = int(slot_str.replace("Slot ", "").strip())

                            atribuicoes.append([nome, disciplina, dia_semana.strip(), slot])

                    # Criação da escala
                    escala = Escala(atribuicoes)
                    self.repositorio_escala.createMemento(escala)

                    text = ""
                    text += "criou uma escala"
                    text += f"\n{escala_str}"
                    self.tela.set_conteudo(text)


                case "main":
                    self.tela = UIFactory().generateMainUI()
                    
                case _:
                    self.tela.set_conteudo("opção não existe!")
                    self.tela.set_escala(self.repositorio_escala.readEscala())
            
            self.tela.show()

            if choice == "main":
                return
            
            choice = input("")
    
    def _colaboradorSystem(self):
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

    def _disciplinaSystem(self):
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

    def _relatorioSystem(self):
        choice = input("")

        while(True):
            match choice.lower():
                case "criar":
                    # Memento previous escala
                    self.relatorio_template.gerar_relatorio(CSV_ColaboradorDAO(), CSV_EscalaDAO())
                    self.tela.set_conteudo("criando relatório")
                case "main":
                    self.tela = UIFactory().generateMainUI()
                case _:
                    self.tela.set_conteudo("opção não existe!")
            
            self.tela.show()

            if choice == "main":
                return
            
            choice = input("")
    
sistema = SistemaEscala()
sistema.runSystem()