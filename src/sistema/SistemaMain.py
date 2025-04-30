from sistema.SistemaEscala import SistemaEscala
from sistema.sistema import Sistema
from sistema.SistemaColaborador import SistemaColaborador
from sistema.SistemaDisciplina import SistemaDisciplina
from sistema.SistemaRelatorio import SistemaRelatorio
from ui.UIFactory import UIFactory


class SistemaMain(Sistema):
    def __init__(self):
        self.tela = UIFactory().generateMainUI()
        super().__init__()

    def runSystem(self):
        self._show_tela()

        while(True):
            self.sistema = None
            choice = input()
            match choice.lower():
                case '1':
                    self.sistema = SistemaEscala()
                case '2':
                    self.sistema = SistemaColaborador()
                case '3':
                    self.sistema = SistemaDisciplina()
                case '4':
                    self.sistema = SistemaRelatorio()
                case '0':
                    print('Saindo do sistema...')
                case _:
                    self.tela.set_conteudo("Opção inválida! Tente novamente.")
                    self._show_tela()
                    continue
            
            if choice == '0':
                break

            if self.sistema:
                self.sistema.runSystem()
