from commands.Command import Command
from persistencia.entidades.Escala import Escala


class EscalaCreateCommand(Command):

    def execute(self, sistema):
        escala_str = sistema.solver_adapter.solve()  # isso retorna a string como a que você mandou

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
        sistema.repositorio_escala.createMemento(escala)

        text = ""
        text += "criou uma escala"
        text += f"\n{escala_str}"
        sistema.tela.set_conteudo(text)