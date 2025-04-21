# src/ui/EscalaUI.py
from .UIInterface import UIInterface
import os

class EscalaUI(UIInterface):

    def __init__(self):
        self._escala = None
        self._conteudo = ""

    def set_escala(self, escala):
        self._escala = escala
    
    def set_conteudo(self, conteudo):
        self._conteudo = conteudo

    def show(self):
        # Implementação para exibir a interface de Escala
        os.system('clear')
        print("\nInterface Escala")
        print("back.    volta para escala antecessora")
        print("forward. avança para escala sucessora")
        print("export.  exporta a escala atual")
        print("main.    volta para a tela principal")
        print()
        print(self._conteudo)

        print(self._escala)
