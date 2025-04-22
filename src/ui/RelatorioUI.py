# src/ui/EscalaUI.py
from .UIInterface import UIInterface
import os

class RelatorioUI(UIInterface):

    def __init__(self):
        self._relatorio = None
        self._conteudo = ""

    def set_relatorio(self, relatorio):
        self._relatorio = relatorio
    
    def set_conteudo(self, conteudo):
        self._conteudo = conteudo

    def show(self):
        # Implementação para exibir a interface de Escala
        os.system('clear')
        print("\nRelatório atual")
        print(self._relatorio)
        print()
        print("criar.    gera novo relatório")
        print("exportar. exporta relatório atual")
        print("main.     volta para a tela principal")
        print(self._conteudo)
