from persistencia.persistenciaFactories.PersistenciaFactory import PersistenciaFactory
from relatorio.RelatorioFactory import RelatorioFactory
from solvers.AdapterFactory import AdapterFactory
from ui.UIFactory import UIFactory


class SistemaEscala:
    
    def __init__(self):        
        self.repositorio_colaborador = PersistenciaFactory().getColaboradorRepository()
        self.relatorio_template = RelatorioFactory().generate_relatorio_CSV()
        self.repositorio_escala = PersistenciaFactory().getEscalaRepository()
        self.solver_adapter = AdapterFactory().generateSolverAdapterMIP()

    def runSystem(self):
        while(True):
            choice = input('Escolha que tela você deseja visualizar\nOpções: Main, Escala e CC\nDigite 0 para sair\n--> ')

            match choice.lower():
                case 'main':
                    tela = UIFactory().generateMainUI()
                case 'escala':
                    tela = UIFactory().generateEscalaUI()
                case 'cc':
                    tela = UIFactory().generateCCUI()
                case '0':
                    print('Saindo do sistema...')
                    break
                case _:
                    print('Tela não existente!')
                    continue

            tela.show()

    def gerarRelatorio(self):
        self.relatorio_template.gerar_relatorio()
    
sistema = SistemaEscala()
sistema.runSystem()