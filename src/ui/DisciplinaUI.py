# src/ui/DisciplinaUI.py
from .UIInterface import UIInterface
import os

class DisciplinaUI(UIInterface):
    def __init__(self):
        self._conteudo = ""
    
    def set_conteudo(self, conteudo):
        self._conteudo = conteudo

    def show(self):
        # Implementação para exibir a interface de Escala
        os.system('clear')
        print("\nInterface Disciplina")
        print("criar.    cria nova disciplina")
        print("deletar.  deleta disciplina existente")
        print("buscar.   busca disciplina por id")
        print("tudo.     mostra todas as disciplinas")
        print("editar.   edita uma disciplina específico")
        print("main.     volta para a tela principal")
        print()
        print(self._conteudo)