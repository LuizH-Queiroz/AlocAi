# src/ui/MainWindowUI.py
from .UIInterface import UIInterface
from .UIFactory import UIFactory

class MainWindowUI(UIInterface):
    def show(self):
        while True:
            print("\nMenu Principal")
            print("1. Adicionar Colaborador")
            print("2. Ver Escala")
            print("3. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                print("Exibindo a interface de Cadastro de Colaborador")
            elif escolha == '2':
                print("Exibindo a interface de Escala")
            elif escolha == '3':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")
