import pandas as pd
from .professor import Professor

class Data:
    def __init__(self):
        self.professores = []  # Lista de objetos Professor
        self.nome_para_id_disciplina = dict()  # nome_disciplina -> id
        self.id_para_nome_disciplina = dict()  # id -> nome_disciplina
        self.horarios_das_disciplinas = dict()  # id_disciplina -> [slots permitidos]

    def load(self):
        self.load_disciplinas()
        self.load_professores()

    def load_disciplinas(self):
        file = 'solvers/School_timetabling_main/Data/VALIDAÇÃO/disciplinas.csv'
        df = pd.read_csv(file)

        # Inicializa os dicionários de mapeamento
        self.nome_para_id_disciplina = {}
        self.id_para_nome_disciplina = {}
        self.horarios_das_disciplinas = {}

        for i, row in df.iterrows():
            nome_disciplina = row['DISCIPLINA']
            id_disc = i  # ou use outro identificador, se necessário

            # Preenche os dois mapeamentos
            self.nome_para_id_disciplina[nome_disciplina] = id_disc
            self.id_para_nome_disciplina[id_disc] = nome_disciplina

            # Converte os slots permitidos
            slots = [int(s) for s in str(row['SLOTS']).split(',') if s.strip().isdigit()]
            self.horarios_das_disciplinas[id_disc] = slots


    def load_professores(self):
        file = 'solvers/School_timetabling_main/Data/VALIDAÇÃO/professores.csv'
        df = pd.read_csv(file)

        for i, row in df.iterrows():
            nome = row['NOME']
            disciplinas_str = row['DISCIPLINAS'].split(',')
            disciplinas = [self.nome_para_id_disciplina[d.strip()] for d in disciplinas_str if d.strip() in self.nome_para_id_disciplina]
            slots = [int(s) for s in str(row['SLOTS']).split(',') if s.strip().isdigit()]

            # Agora passamos todos os parâmetros necessários para o Professor
            professor = Professor(nome, i, disciplinas, slots)

            self.professores.append(professor)
