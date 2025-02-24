import os
import time

def clear_sleep(t=0.5):
  os.system('cls' if os.name == 'nt' else 'clear')
  time.sleep(t)

os.system('cls' if os.name == 'nt' else 'clear')
print("\nBem vindo ao AlocAI!")
while True:
  clear_sleep()
  print("""\nBem vindo ao AlocAI!"
\nSelecione a opção desejada:
1- Listar funcionários
2- Cadastrar funcionário
3- Sair do sistema""")
  try:
    opcao = int(input("Opção: "))
  except ValueError as e:
    print("\nOpção inválida. Tente novamente.")
    continue
  
  if opcao == 3:
    print("\nObrigado por usar nosso sistema!", end="\n\n")
    break
