import pandas as pd

df = pd.ExcelFile("Data/PLANILHA CH PROFESSORES D'ÁVILA LINS.xlsx")

geral = df.parse('PLANILHA GERAL')
professor = df.parse('PROFESSOR')

professor = professor.replace('ARTE', 'ARTES')
professor = professor.replace('EDUCAÇÃO FÍSICA', 'ED. FÍSICA')

complemento = dict()
sigla = []

for _, row in geral.iterrows():
    if row['PROFESSOR'] not in complemento:
        complemento[row['PROFESSOR']] = row['COMPLEMENTO']
    
    if 'VI' in row['SÉRIE']:
        serie = 'VI'
    elif 'V' in row['SÉRIE']:
        serie = 'V'
    else:
        serie = row['SÉRIE'][0]

    turma = serie + row['TURMA'] + row['TURNO'][0]
    sigla.append(turma)

resposta = []

for _, row in professor.iterrows():
    resposta.append(complemento[row['PROFESSOR']])

professor['COMPLEMENTO'] = resposta
geral['siglaTurma'] = sigla

with pd.ExcelWriter(df, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    professor.to_excel(writer, sheet_name='PROFESSOR', index=False)
    geral.to_excel(writer, sheet_name='PLANILHA GERAL', index=False)