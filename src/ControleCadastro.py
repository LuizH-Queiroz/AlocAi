from Colaborador import Colaborador

class ControleCadastro:
    def __init__(self):
      # Inicia com esses funcionários para demonstração
      self.colaboradores = [
        Colaborador("João", 27456),
        Colaborador("Maria", 14149)
      ]
    
    def listar_colaboradores(self):
      for colaborador in self.colaboradores:
        print() # Linha em branco antes do registro do colaborador
        print(f"Nome: {colaborador.nome}")
        print(f"Número de Registro: {colaborador.numeroRegistro}")
    
    def cadastrar_colaborador(self):
      nome = input("Nome: ")
      numeroRegistro = input("Número de Registro: ")
      self.colaboradores.append(Colaborador(nome, numeroRegistro))
      print("\nColaborador cadastrado com sucesso")