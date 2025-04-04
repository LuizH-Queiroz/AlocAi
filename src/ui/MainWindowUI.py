# src/ui/MainWindowUI.py
from .UIInterface import UIInterface


class MainWindowUI(UIInterface):
    def show(self):
        while True:
            print("\nMenu Principal")
            print("1. Adicionar Colaborador")
            print("2. Ver Escala")
            print("3. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.adicionar_colaborador()
            elif escolha == '2':
                self.ver_escala()
            elif escolha == '3':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")
