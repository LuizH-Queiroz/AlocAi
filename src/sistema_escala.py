from persistencia.persistenciaFactories.PersistenciaFactory import PersistenciaFactory
from relatorio.RelatorioFactory import RelatorioFactory
from solvers.AdapterFactory import AdapterFactory
from ui.UIFactory import UIFactory
from persistencia.entidades.Colaborador import Colaborador  
from abc import abstractmethod, ABC

class SistemaEscala:
    
    def __init__(self):        
        self.repositorio_colaborador = PersistenciaFactory().getColaboradorRepository()
        self.relatorio_template = RelatorioFactory().generate_relatorio_CSV()
        self.repositorio_escala = PersistenciaFactory().getEscalaRepository()
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
                    # self.command = SistemaEscala.EscalaCommand()
                case '2':
                    self.tela = UIFactory().generateCCUI()
                    # self.command = SistemaEscala.ColaboradorCommand()
                case '3':
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
                    self._relatorioSystem()
                case _:
                    continue

    # class Command(ABC):
    #     @abstractmethod
    #     def execute(self):
    #         pass
    
    # class EscalaCommand(Command):

    def _escalaSystem(self):
        choice = input("")

        while(True):
            match choice.lower():
                case "back":
                    memento = self.repositorio_escala.previousMemento()
                    text = ""
                    text += "voltou uma escala"
                    text += f"\n{memento}"
                    self.tela.set_conteudo(text)

                case "forward":
                    memento = self.repositorio_escala.nextMemento()
                    text = ""
                    text += "avançou uma escala"
                    text += f"\n{memento}"
                    self.tela.set_conteudo(text)

                case "create":
                    escala = self.solver_adapter.solve()
                    memento = self.repositorio_escala.createMemento(escala)

                    text = ""
                    text += "criou uma escala"
                    text += f"\n{memento}"
                    self.tela.set_conteudo(text)

                case "export":
                    # self.relatorio_template.gerar_relatorio()
                    self.tela.set_conteudo("exportou relatorio")

                case "main":
                    self.tela = UIFactory().generateMainUI()
                    
                case _:
                    self.tela.set_conteudo("opção não existe!")
            
            self.tela.show()

            if choice == "main":
                return
            
            choice = input("")
    
    # def execute(self):
    #     return self.EscalaSystem()
    
    # class ColaboradorCommand(Command):
    def _colaboradorSystem(self):
        choice = input("")

        while(True):
            match choice.lower():
                case "criar":
                    # Memento previous escala
                    print("criando colaborador")

                    nome = input("nome: ")
                    id = int(input("id: "))
                    turno = input("turno: ")
                    colaborador = Colaborador(nome, id, turno.split(','))

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
                    id = input("id do colaborador a ser editado: ")
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
                            print("Turnos:", end=" ")
                            print(", ".join(str(turno) for turno in colaborador.getTurnos()))
                            print("-" * 30)

                            print(colaborador)
                            print(type(colaborador))

                            campo = input("campo a ser editado (nome, id, turnos): ")
                            if campo == "nome":
                                novo_nome = input("novo nome: ")
                                self.repositorio_colaborador.updateColaborador(
                                    id,
                                    Colaborador(
                                        novo_nome,
                                        colaborador.getId(),
                                        colaborador.getTurnos()
                                    )
                                )
                            elif campo == "id":
                                novo_id = int(input("novo id: "))
                                colaborador.setId(novo_id)
                                self.repositorio_colaborador.updateColaborador(
                                    id,
                                    Colaborador(
                                        colaborador.getNome(),
                                        novo_id,
                                        colaborador.getTurnos()
                                        )
                                )
                            elif campo == "turnos":
                                novos_turnos = input("novos turnos (separados por vírgula): ")
                                novos_turnos = novos_turnos.split(',')
                                colaborador.setTurnos(novos_turnos)
                                self.repositorio_colaborador.updateColaborador(
                                    id,
                                    Colaborador(
                                        colaborador.getNome(),
                                        colaborador.getId(),
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

    
    # def createColaborador(self, colaborador):
    #     self._colaboradorDAO.create(colaborador)

    # def deleteColaborador(self, id: int):
    #     self._colaboradorDAO.delete(id)

    # def readColaborador(self, id: int):
    #     return self._colaboradorDAO.read(id)

    # def readAllColaborador(self):
    #     return self._colaboradorDAO.readAll()

    # def updateColaborador(self, id: int, novosDados):
    #     self._colaboradorDAO.update(id, novosDados)

    # def execute(self):
    #     return self.ColaboradorSystem()

    # def execute(self):
    #     return self.SolverSystem()
    
    # class RelatorioCommand(Command):
    def _relatorioSystem(self):
        choice = input("")

        while(True):
            match choice.lower():
                case "criar":
                    # Memento previous escala
                    self.tela.set_conteudo("criando relatório")
                case "exportar":
                    # Memento previous escala
                    self.tela.set_conteudo("exportando relatório")
                case "main":
                    self.tela = UIFactory().generateMainUI()
                case _:
                    self.tela.set_conteudo("opção não existe!")
            
            self.tela.show()

            if choice == "main":
                return
            
            choice = input("")

    # def execute(self):
    #     return self.RelatorioSystem()
    
sistema = SistemaEscala()
sistema.runSystem()