from src.solvers import AdapterFactory


class SistemaEscala:
    
    def __init__(self):
        # ui_factory = UiFactory
        adapter_factory = AdapterFactory()
        # persistencia_factory = PersistenciaFactory()
        # template_factory = TemplateFactory()
        # repositorio_colaborador = ColaboradorRepository()
        # relatorio_template = RelatorioTemplate()
        # repositorio_escala = EscalaRepository()
        # UI_show = UIInterface()
        # solver = Solver()

    # def runSystem(self):
    #     while(True):
    #         choice = input('Escolha que tela você deseja visualizar\nOpções: Main, Escala e CC\n--> ')

    #         match choice.lower():
    #             case 'main':
    #                 tela = UI_show.generateMainUI()
    #             case 'escala':
    #                 tela = UI_show.generateEscalaUI()
    #             case 'cc':
    #                 tela = UI_show.generateCCUI()
    #             case _:
    #                 print('Tela não existente!')
    #                 continue

    #         tela.show()

    # def gerarRelatorio(self):
    #     relatorio_template.gerarRelatorio()