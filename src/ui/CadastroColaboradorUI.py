# src/ui/CadastroColaboradorUI.py
from .UIInterface import UIInterface
import os

class CadastroColaboradorUI(UIInterface):
    def __init__(self):
        self._conteudo = ""
    
    def set_conteudo(self, conteudo):
        self._conteudo = conteudo

    def show(self):
        # Implementação para exibir a interface de Escala
        os.system('clear')
        print("\nInterface Escala")
        print("criar.    volta para escala antecessora")
        print("deletar.  avança para escala sucessora")
        print("buscar.   exporta a escala atual")
        print("tudo.     exporta a escala atual")
        print("editar.   exporta a escala atual")
        print("main.     volta para a tela principal")
        print()
        print(self._conteudo)