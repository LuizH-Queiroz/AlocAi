from Funcionario import Funcionario

class ControleCadastro:
    def __init__(self):
      # Inicia com esses funcionários para demonstração
      self.funcionarios = [Funcionario("João", 25, "M"), Funcionario("Maria", 30, "F")]
    
    def listar_funcionarios(self):
      for funcionario in self.funcionarios:
        print(f"Nome: {funcionario.nome}\nIdade: {funcionario.idade}\nGênero: {funcionario.genero}\n")
    
    def cadastrar_funcionario(self):
       nome = input("Nome: ")
       idade = input("Idade: ")
       genero = input("Genero (M/F): ")
       self.funcionarios.append(Funcionario(nome, idade, genero))
       print("\nFuncionário cadastrado com sucesso")