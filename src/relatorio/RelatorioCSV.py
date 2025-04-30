import pandas as pd
from .RelaorioTemplate import RelatorioTemplate

class RelatorioCSV(RelatorioTemplate):

    def _get_colaboradores(self, dao_colaboradores):
        return dao_colaboradores.readAll()
    
    def _get_escala_geral(self, dao_escala):
        return dao_escala.read()
    
    def _save_csv(self, df: pd.DataFrame, path: str):
        df.to_csv(path, index=False)
    
    def _imprime_colaboradores(self, colaboradores):
        colaboradores = [[colaborador.getId(), colaborador.getNome(), colaborador.getDisciplinas(), colaborador.getTurnos()] for colaborador in colaboradores]
        colunas = ['id', 'nome', 'disciplinas', 'turnos']
        df = pd.DataFrame(colaboradores, columns=colunas)
        print(df.to_string(index=False))
        self._save_csv(df, 'dados_colaboradores.csv')

    def _imprime_escala(self, escala):
        colunas = ['id', 'disciplina', 'dia_semana', 'horario']
        df = pd.DataFrame(escala, columns=colunas)
        print(df.to_string(index=False))
        self._save_csv(df, 'dados_escala.csv')

    def _imprime_relatorio(self, colaboradores, escala):
        print("CSV")
        self._imprime_colaboradores(colaboradores)
        self._imprime_escala(escala)
        input()
