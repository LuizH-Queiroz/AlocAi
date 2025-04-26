import pandas as pd
import openpyxl

file = 'Data/VALIDAÇÃO/disponibilidade_profs_corrigida.csv'
df_csv = pd.read_csv(file, encoding='latin1')

file = "Data/PLANILHA CH PROFESSORES D'ÁVILA LINS.xlsx"
df_excel = pd.ExcelFile(file).parse('PROFESSOR')

dict_prof = dict()

for _, row in df_csv.iterrows():
    nome = row['PROFESSOR']

    if nome in dict_prof: continue

    disciplina = row['DISCIPLINA']

    dict_prof[nome] = disciplina

dict_prof['ADRIANA DOMINGOS'] = 'INGLÊS'

for _, row in df_excel.iterrows():
    nome = row['PROFESSOR']

    if nome not in dict_prof:
        print(f'Inconsistência nos dados -> {nome}')
        continue

    disciplina = row['DISCIPLINA PRIORITÁRIA']

    if disciplina != dict_prof[nome]:
        print(f'Inconsistência nos dados (disciplina) -> {nome} ({disciplina} / {dict_prof[nome]})')

columns = ['MANHÃ', 'TARDE', 'NOITE', 'SEG-M', 'TER-M', 'QUA-M', 'QUI-M', 'SEX-M', 'SEG-T', 'TER-T', 'QUA-T', 'QUI-T', 'SEX-T', 'SEG-N', 'TER-N', 'QUA-N', 'QUI-N', 'SEX-N', 'DISCIPLINA PRIORITÁRIA', 'DISCIPLINA 2', 'DISCIPLINA 3', 'DISCIPLINA 4']
df_excel.drop(columns=columns, inplace=True)

df_excel['DISCIPLINA'] = df_excel['PROFESSOR'].map(dict_prof)

columns = ['DISCIPLINA', 'VÍNCULO']
df_csv.drop(columns=columns, inplace=True)

file_name = 'Data/VALIDAÇÃO/professor.csv'
df_excel.to_csv(file_name)

file_name = 'Data/VALIDAÇÃO/disponibilidade_profs_corrigida.csv'
df_csv.to_csv(file_name)