# src/ui/MainWindowUI.py
from .UIInterface import UIInterface
import os

class MainWindowUI(UIInterface):

    def __init__(self):
        self._conteudo = ""
    
    def set_conteudo(self, conteudo):
        self._conteudo = conteudo

    def show(self):
        # while True:
        os.system('clear')
        print("\nMenu Principal")
        print("1. interface da Escala")
        print("2. interface do Colaborador")
        print("3. ir para resolvedor")
        print("4. gerar relatório")
        print("0. Sair")
        print()
        print(self._conteudo)

            # escolha = input("Escolha uma opção: ")

            # if escolha == '1':
            #     print("Exibindo a interface de Cadastro de Colaborador")
            # elif escolha == '2':
            #     print("Exibindo a interface de Escala")
            # elif escolha == '3':
            #     print("Saindo do sistema...")
            #     break
            # else:
            #     print("Opção inválida! Tente novamente.")
