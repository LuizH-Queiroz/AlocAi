import pandas as pd

df = pd.ExcelFile("Data/PLANILHA CH PROFESSORES D'ÁVILA LINS.xlsx")

geral = df.parse('PLANILHA GERAL')

turmas = list(set(geral['siglaTurma'].to_list()))
coluna = []
turnos = {'M': 'MANHÃ', 'T': 'TARDE', 'N': 'NOITE'}

for turma in turmas:
    linha = dict()
    i = 1

    if turma[0] == 'V':
        linha['Modalidade'] = 'EJA'
        if turma[1] == 'I':
            linha['Série'] = 'CICLO ' + turma[0] + turma[1]
            i += 1
        else:
            linha['Série'] = 'CICLO ' + turma[0]
    elif turma[0] == '9':
        linha['Modalidade'] = 'FUNDAMENTAL'
        linha['Série'] = turma[0] + 'º'
    else:
        linha['Modalidade'] = 'MÉDIO REGULAR'
        linha['Série'] = turma[0] + 'º'

    linha['Turma'] = turma[i]
    linha['Turno'] = turnos[turma[i + 1]]

    coluna.append(linha)

turmas = pd.DataFrame(coluna)

with pd.ExcelWriter(df, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    turmas.to_excel(writer, sheet_name='SALAS', index=False)