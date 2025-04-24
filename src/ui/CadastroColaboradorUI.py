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
        print("\nInterface Colaborador")
        print("criar.    cria novo colaborador")
        print("deletar.  deleta colaborador existente")
        print("buscar.   busca colaborador por id")
        print("tudo.     mostra todos os colaboradores")
        print("editar.   edita um colaborador específico")
        print("main.     volta para a tela principal")
        print()
        print(self._conteudo)