import pandas as pd


file = 'Data/VALIDAÇÃO/disponibilidade_profs_corrigida.csv'
df_professores = pd.read_csv(file)

columns = ['SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA']
turnos = {'MANHÃ': 0, 'TARDE': 6, 'NOITE': 12}
dias = {'SEGUNDA': 0, 'TERÇA': 18, 'QUARTA': 36, 'QUINTA': 54, 'SEXTA': 72}

disponibilidade_prof = dict()

for _, row in df_professores.iterrows():
    professor = row['PROFESSOR']

    if professor not in disponibilidade_prof:
        disponibilidade_prof[professor] = []

    for column in columns:
        if row[column]:
            horario = turnos[row['TURNO']] + dias[column] + row['HORARIO'] - 1
            disponibilidade_prof[professor].append(horario)


file = 'Data/VALIDAÇÃO/horario.csv'
df = pd.read_csv(file, encoding='latin1')

colunas = ['SEG', 'TER', 'QUA', 'QUI', 'SEX']
dias = {'SEG': 0, 'TER': 18, 'QUA': 36, 'QUI': 54, 'SEX': 72}
conversao = {'SEG': 'SEGUNDA', 'TER': 'TERÇA', 'QUA': 'QUARTA', 'QUI': 'QUINTA', 'SEX': 'SEXTA'}

for _, row in df.iterrows():
    for coluna in colunas:
        info = row[coluna]
        _, professor = info.split(' Prof')
        professor = professor.split('. ')[1]

        horario = turnos[row['TURNO']] + dias[coluna] + row['AULAS'] - 1
        
        if horario not in disponibilidade_prof[professor]:
            print(f"{professor} -> {coluna} / {row['TURNO']} / {row['AULAS']}\n")
            
            filtro = (df_professores['PROFESSOR'] == professor) & (df_professores['TURNO'] == row['TURNO']) & (df_professores['HORARIO'] == row['AULAS'])
            if not filtro.any():
                print('Algo deu errado!')
            else:
                df_professores.loc[filtro, conversao[coluna]] = 1

file = 'Data/VALIDAÇÃO/disponibilidade_profs_corrigida.csv'
df_professores.to_csv(file)