import pandas as pd

class Write_solution:

    def __init__(self, data) -> None:
        self.data = data
        self.solution = []
        self.slots_por_dia = 3
        self.dias = 5
        self.total_slots = self.slots_por_dia * self.dias
        self.get_solution()
        self.get_relacao()

    def get_solution(self):
        """Lê a solução do arquivo e armazena as alocações."""
        with open('solvers/School_timetabling_main/Solution/Solucao.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.rstrip('\n')
                self.solution.append(line)

    def get_relacao(self):
        """Relaciona os professores, disciplinas e slots."""
        self.relacao_slots = [[] for _ in range(self.total_slots)]  # Lista de slots
        self.relacao_professores = [[] for _ in range(len(self.data.professores))]  # Professores

        for var in self.solution:
            _, p, m, s = var.split('_')  # Professor, disciplina, slot
            p, m, s = int(p), int(m), int(s)

            # Relaciona os slots com os professores e disciplinas
            self.relacao_slots[s].append([p, m])
            self.relacao_professores[p].append([m, s])

    def write_excel_dia_slot(self):
        """Gera um arquivo Excel com as alocações ordenadas por (dia_da_semana, slot)."""
        # Define o nome do arquivo Excel
        excel_file = 'solvers/School_timetabling_main/Solution/Solucao_por_dia_slot.xlsx'

        dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

        # Criação de uma lista para armazenar as alocações
        alocacoes = []

        # Preenche a lista de alocações com os dados
        for var in self.solution:
            if not var.startswith('x_'):
                continue

            _, p, m, s = var.split('_')
            p, m, s = int(p), int(m), int(s)

            professor = self.data.professores[p].nome
            nome_disciplina = self.data.id_para_nome_disciplina[m]
            dia = dias[s // self.slots_por_dia]  # Calcula o dia da semana
            slot_do_dia = s % self.slots_por_dia + 1  # Calcula o slot no dia

            # Adiciona a alocação à lista
            alocacoes.append([professor, nome_disciplina, dia, slot_do_dia])

        # Ordena pela tupla (dia_da_semana, slot)
        alocacoes.sort(key=lambda x: (dias.index(x[2]), x[3]))

        # Criação de um DataFrame com os dados
        df_alocacoes = pd.DataFrame(alocacoes, columns=["Professor", "Disciplina", "Dia", "Slot"])

        # Criação do arquivo Excel com os dados
        with pd.ExcelWriter(excel_file, engine='openpyxl', mode='w') as writer:
            df_alocacoes.to_excel(writer, index=False)

        print(f"Planilha Excel gerada com sucesso em: {excel_file}")

    def write_excel_professor(self):
        """Gera um arquivo Excel com as alocações ordenadas por (professor, dia, slot)."""
        # Define o nome do arquivo Excel
        excel_file = 'solvers/School_timetabling_main/Solution/Solucao_por_professor_dia_slot.xlsx'

        dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

        # Criação de uma lista para armazenar as alocações
        alocacoes = []

        # Preenche a lista de alocações com os dados
        for var in self.solution:
            if not var.startswith('x_'):
                continue

            _, p, m, s = var.split('_')
            p, m, s = int(p), int(m), int(s)

            professor = self.data.professores[p].nome
            nome_disciplina = self.data.id_para_nome_disciplina[m]
            dia = dias[s // self.slots_por_dia]  # Calcula o dia da semana
            slot_do_dia = s % self.slots_por_dia + 1  # Calcula o slot no dia

            # Adiciona a alocação à lista
            alocacoes.append([professor, nome_disciplina, dia, slot_do_dia])

        # Ordena pela tupla (professor, dia, slot)
        alocacoes.sort(key=lambda x: (x[0], dias.index(x[2]), x[3]))

        # Criação de um DataFrame com os dados
        df_alocacoes = pd.DataFrame(alocacoes, columns=["Professor", "Disciplina", "Dia", "Slot"])

        # Criação do arquivo Excel com os dados
        with pd.ExcelWriter(excel_file, engine='openpyxl', mode='w') as writer:
            df_alocacoes.to_excel(writer, index=False)

        print(f"Planilha Excel gerada com sucesso em: {excel_file}")
