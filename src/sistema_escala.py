from persistencia.persistenciaFactories.PersistenciaFactory import PersistenciaFactory
from relatorio.RelatorioFactory import RelatorioFactory
from solvers.AdapterFactory import AdapterFactory
from ui.UIFactory import UIFactory
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
                    # Memento previous escala
                    self.tela.set_conteudo("voltou uma escala")
                case "forward":
                    # self.tela = Memento next escala
                    self.tela.set_conteudo("avançou uma escala")
                case "create":
                    # self.tela = Memento next escala
                    self.tela.set_conteudo("criou uma escala")
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
                    self.tela.set_conteudo("criando colaborador")
                case "deletar":
                    # self.tela = Memento next escala
                    self.tela.set_conteudo("deletando colaborador")
                case "buscar":
                    # self.relatorio_template.gerar_relatorio()
                    self.tela.set_conteudo("buscando colaborador")
                case "tudo":
                    # self.relatorio_template.gerar_relatorio()
                    self.tela.set_conteudo("mostrando todos os colaboradores")
                case "editar":
                    # self.relatorio_template.gerar_relatorio()
                    self.tela.set_conteudo("editando colaborador")
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