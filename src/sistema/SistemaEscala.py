from persistencia.entidades.Escala import Escala
from sistema.sistema import Sistema
from ui.UIFactory import UIFactory


class SistemaEscala(Sistema):
    def __init__(self):
        self.tela = UIFactory().generateEscalaUI()
        super().__init__()

    def runSystem(self):
        self._show_tela()
        
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

    def _show_tela(self):
        self.tela.set_escala(self.repositorio_escala.readEscala())
        self.tela.show()