from Colaborador import Colaborador

class ControleCadastro:
    def __init__(self):
      # Inicia com esses funcionários para demonstração
      self.colaboradors = [Colaborador("João", 25, "M"), Colaborador("Maria", 30, "F")]
    
    def listar_colaboradores(self):
      for colaborador in self.colaboradors:
        print(f"Nome: {colaborador.nome}\nIdade: {colaborador.idade}\nGênero: {colaborador.genero}\n")
    
    def cadastrar_colaborador(self):
       nome = input("Nome: ")
       idade = input("Idade: ")
       genero = input("Genero (M/F): ")
       self.colaboradors.append(Colaborador(nome, idade, genero))
       print("\nFuncionário cadastrado com sucesso")