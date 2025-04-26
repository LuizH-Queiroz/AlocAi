import pandas as pd


file = 'Data/VALIDAÇÃO/horario.csv'
df = pd.read_csv(file, encoding='latin1')

file = 'Data/VALIDAÇÃO/professor.csv'
df_professores = pd.read_csv(file)

prof_disciplina = dict()

for _, row in df_professores.iterrows():
    nome = row['PROFESSOR']
    disciplina = row['DISCIPLINA']

    prof_disciplina[nome] = disciplina.split('/')

colunas = ['TURNO', 'SÉRIE', 'TURMA', 'AULAS']
df = df.drop(columns=colunas)

colunas = ['SEG', 'TER', 'QUA', 'QUI', 'SEX']

for i, row in df.iterrows():
    for coluna in colunas:
        info = row[coluna]
        materia, professor = info.split(' Prof')
        professor = professor.split('. ')[1]

        if professor not in prof_disciplina:
            print(f'Inconsistência nos dados -> {professor}')

        if materia not in prof_disciplina[professor]:
            prof_disciplina[professor].append(materia)

prof_disciplina = {professor: '/'.join(disciplinas) for professor, disciplinas in prof_disciplina.items()}

df_professores['DISCIPLINA'] = df_professores['PROFESSOR'].map(prof_disciplina)

file = 'Data/VALIDAÇÃO/professor.csv'
df_professores.to_csv(file)