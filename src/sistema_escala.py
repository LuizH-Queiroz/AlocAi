from src.persistencia.persistenciaFactories.PersistenciaFactory import PersistenciaFactory
from src.persistencia.repositorios import ColaboradorRepository, EscalaRepository
from src.relatorio.RelaorioTemplate import RelatorioTemplate
from src.solvers.AdapterFactory import AdapterFactory


class SistemaEscala:
    
    def __init__(self):
        # UI_factory = UiFactory
        self.adapter_factory = AdapterFactory()
        self.persistencia_factory = PersistenciaFactory()
        # template_factory = TemplateFactory()
        
        self.repositorio_colaborador = self.persistencia_factory.getColaboradorRepository()
        self.relatorio_template = RelatorioTemplate()
        self.repositorio_escala = self.persistencia_factory.getEscalaRepository()
        # UI_show = UIInterface()
        self.solver_adapter = self.adapter_factory.generateSolverAdapterMIP()

    def runSystem(self):
        while(True):
            choice = input('Escolha que tela você deseja visualizar\nOpções: Main, Escala e CC\n--> ')

            match choice.lower():
                case 'main':
                    tela = self.UI_show.generateMainUI()
                case 'escala':
                    tela = self.UI_show.generateEscalaUI()
                case 'cc':
                    tela = self.UI_show.generateCCUI()
                case _:
                    print('Tela não existente!')
                    continue

            tela.show()

    def gerarRelatorio(self):
        self.relatorio_template.gerarRelatorio()