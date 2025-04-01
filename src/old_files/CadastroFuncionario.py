import time

from ControleCadastro import ControleCadastro
from utils import clear_sleep

controle = ControleCadastro()

while True:
  clear_sleep()

  print("""Bem vindo ao AlocAI!
\nSelecione a opção desejada:
1- Listar funcionários
2- Cadastrar funcionário
3- Sair do sistema""")
  
  try:
    # Valida se o input é um número inteiro
    opcao = int(input("Opção: "))
  except ValueError as e:
    print("\nOpção inválida, por favor digite apenas o número da opção desejada", end="\n\n")
    time.sleep(2)
    continue
  
  if opcao == 1:
    clear_sleep()
    print("Lista de funcionários", end="\n\n")
    controle.listar_colaboradores()
    input('\nPressione "ENTER" para continuar')

  elif opcao == 2:
    clear_sleep()
    print("Cadastro de funcionário", end="\n\n")
    controle.cadastrar_colaborador()

  elif opcao == 3:
    print("\nObrigado por usar nosso sistema!", end="\n\n")
    break

  else:
    print("\nOpção inválida, por favor selecione uma das opções do menu", end="\n\n")
    time.sleep(2)
