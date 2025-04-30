# src/ui/EscalaUI.py
from .UIInterface import UIInterface
import os

class EscalaUI(UIInterface):

    def __init__(self):
        self._escala = None
        self._conteudo = ""

    def set_escala(self, atribuicoes):
        self._escala = atribuicoes
        if atribuicoes:
            linhas_formatadas = []
            for nome, disciplina, dia_semana, slot in atribuicoes:
                linha = f"{nome} → {disciplina} | {dia_semana} - Slot {slot}"
                linhas_formatadas.append(linha)
            escala_str = '\n'.join(linhas_formatadas)
            self._conteudo += "\n\n--- Escala Atual ---\n" + escala_str
        else:
            self._conteudo += "\n\n--- Escala Atual ---\n(vazia ou não carregada)"

    
    def set_conteudo(self, conteudo):
        self._conteudo = conteudo

    def show(self):
        # Implementação para exibir a interface de Escala
        os.system('clear')
        print("\nInterface Escala")
        print("back.    volta para escala antecessora")
        print("forward. avança para escala sucessora")
        print("create.  cria uma nova escala com os dados atuais")
        print("main.    volta para a tela principal")
        print()
        print(self._conteudo)
