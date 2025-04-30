from persistencia.DAOs.CSV_EscalaDAO import CSV_EscalaDAO
from persistencia.DAOs.CSV_ColaboradorDAO import CSV_ColaboradorDAO
from sistema.sistema import Sistema
from ui.UIFactory import UIFactory


class SistemaRelatorio(Sistema):
    def __init__(self):
        self.tela = UIFactory().generateRelatorioUI()
        super().__init__()

    def runSystem(self):
        self._show_tela()
        
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