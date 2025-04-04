from persistencia.persistenciaFactories.PersistenciaFactory import PersistenciaFactory
from relatorio.RelaorioTemplate import RelatorioTemplate
from solvers.AdapterFactory import AdapterFactory


class SistemaEscala:
    
    def __init__(self):
        # template_factory = TemplateFactory()
        
        self.repositorio_colaborador = PersistenciaFactory.getColaboradorRepository()
        self.relatorio_template = RelatorioTemplate()
        self.repositorio_escala = PersistenciaFactory.getEscalaRepository()
        # UI_show = UIInterface()
        self.solver_adapter = AdapterFactory.generateSolverAdapterMIP()

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