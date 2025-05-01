from mip import Model, xsum, BINARY, MAXIMIZE

class Formulacao:
    def __init__(self, data) -> None:
        self.data = data

        self.P = range(len(data.professores))
        self.M = [data.nome_para_id_disciplina[nome] for nome in data.nome_para_id_disciplina]
        self.S = range(15)  # 5 dias * 3 slots por dia
        self.Sd = [[slot + (dia * 3) for slot in range(3)] for dia in range(5)]

        self.Mp = [professor.disciplinas for professor in self.data.professores]
        self.Sp = [professor.slots for professor in self.data.professores]
        self.Sm = self.data.horarios_das_disciplinas  # dict: disciplina -> [slots permitidos]

        self.slots_por_dia = 3
        self.solution = []

    def print_solution(self):
        solucao = "\nSOLUÇÃO FINAL\n" + "-" * 30 + "\n"
        dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

        for var in self.solution:
            if not var.startswith('x_'):
                continue

            _, p, m, s = var.split('_')
            p, m, s = int(p), int(m), int(s)

            professor = self.data.professores[p].nome
            nome_disciplina = self.data.id_para_nome_disciplina[m]
            dia = dias[s // self.slots_por_dia]
            slot_do_dia = s % self.slots_por_dia + 1

            solucao += f"{professor} → {nome_disciplina} | {dia} - Slot {slot_do_dia}\n"
        
        return solucao

    def save_solution(self):
        with open('solvers/School_timetabling_main/Solution/Solucao.txt', 'w') as f:
            for var in self.solution:
                f.write(f"{var}\n")

    def solve_model(self):
        status = self.model.optimize(max_seconds=3600)

        if self.model.status != self.model.status.OPTIMAL and self.model.status != self.model.status.FEASIBLE:
            return False

        print(f'Status da solução = {self.model.status}')
        print(f"Solution value = {self.model.objective_value:.2f}\n")
        print("Solution:")
        for v in self.model.vars:
            if v.x >= 0.9999:
                print(f"{v.name} = {v.x:.2f}")
                if v.name.startswith('x_'):
                    self.solution.append(v.name)

        self.save_solution()
        return True

    def create_model(self):
        self.model = Model(sense=MAXIMIZE)
from mip import Model, xsum, BINARY, MAXIMIZE

class Formulacao:
    def __init__(self, data) -> None:
        self.data = data

        self.P = range(len(data.professores))
        self.M = [data.nome_para_id_disciplina[nome] for nome in data.nome_para_id_disciplina]
        self.S = range(15)  # 5 dias * 3 slots por dia
        self.Sd = [[slot + (dia * 3) for slot in range(3)] for dia in range(5)]

        self.Mp = [professor.disciplinas for professor in self.data.professores]
        self.Sp = [professor.slots for professor in self.data.professores]
        self.Sm = self.data.horarios_das_disciplinas  # dict: disciplina -> [slots permitidos]

        self.slots_por_dia = 3
        self.solution = []

    def print_solution(self):
        solucao = "\nSOLUÇÃO FINAL\n" + "-" * 30 + "\n"
        dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

        for var in self.solution:
            if not var.startswith('x_'):
                continue

            _, p, m, s = var.split('_')
            p, m, s = int(p), int(m), int(s)

            professor = self.data.professores[p].nome
            nome_disciplina = self.data.id_para_nome_disciplina[m]
            dia = dias[s // self.slots_por_dia]
            slot_do_dia = s % self.slots_por_dia + 1

            solucao += f"{professor} → {nome_disciplina} | {dia} - Slot {slot_do_dia}\n"
        
        return solucao

    def save_solution(self):
        with open('solvers/School_timetabling_main/Solution/Solucao.txt', 'w') as f:
            for var in self.solution:
                f.write(f"{var}\n")

    def solve_model(self):
        status = self.model.optimize(max_seconds=3600)

        if self.model.status != self.model.status.OPTIMAL and self.model.status != self.model.status.FEASIBLE:
            return False

        print(f'Status da solução = {self.model.status}')
        print(f"Solution value = {self.model.objective_value:.2f}\n")
        print("Solution:")
        for v in self.model.vars:
            if v.x >= 0.9999:
                print(f"{v.name} = {v.x:.2f}")
                if v.name.startswith('x_'):
                    self.solution.append(v.name)

        self.save_solution()
        return True

    def create_model(self):
        # 🔄 Aqui está a única modificação necessária: forçar uso do CBC
        self.model = Model(sense=MAXIMIZE, solver_name="CBC")

        # Variáveis
        self.x = {}
        for p in self.P:
            for m in self.Mp[p]:
                for s in self.Sp[p]:
                    if m in self.Sm and s in self.Sm[m]:
                        self.x[p, m, s] = self.model.add_var(name=f"x_{p}_{m}_{s}", var_type=BINARY)

        # Restrição: Um professor só pode estar em um slot por vez
        for p in self.P:
            for s in self.Sp[p]:
                self.model += xsum(self.x[p_, m, s_] for (p_, m, s_) in self.x if p_ == p and s_ == s) <= 1

        # Restrição: No máximo 2 disciplinas por professor por dia
        for p in self.P:
            for d in self.Sd:
                self.model += xsum(self.x[p_, m, s_] for (p_, m, s_) in self.x if p_ == p and s_ in d) <= 2

        # Restrição: Cada disciplina deve ser alocada uma vez em algum professor/slot permitido
        for m in self.M:
            if m in self.Sm:
                for s in self.Sm[m]:
                    self.model += xsum(
                        self.x[p_, m_, s_] for (p_, m_, s_) in self.x if m_ == m and s_ == s
                    ) == 1

        # Função Objetivo
        alocacoes = xsum(
            self.x[p, m, s]
            for (p, m, s) in self.x
        )

        penalidades = xsum(
            1 - xsum(
                self.x[p, m, s]
                for p in self.P if m in self.Mp[p]
                for s in self.Sm.get(m, [])
                if (p, m, s) in self.x
            )
            for m in self.M
        )

        self.model.objective = alocacoes - 1000 * penalidades

        # Variáveis
        self.x = {}
        for p in self.P:
            for m in self.Mp[p]:
                for s in self.Sp[p]:
                    if m in self.Sm and s in self.Sm[m]:
                        self.x[p, m, s] = self.model.add_var(name=f"x_{p}_{m}_{s}", var_type=BINARY)

        # Restrição: Um professor só pode estar em um slot por vez
        for p in self.P:
            for s in self.Sp[p]:
                self.model += xsum(self.x[p_, m, s_] for (p_, m, s_) in self.x if p_ == p and s_ == s) <= 1

        # Restrição: No máximo 2 disciplinas por professor por dia
        for p in self.P:
            for d in self.Sd:
                self.model += xsum(self.x[p_, m, s_] for (p_, m, s_) in self.x if p_ == p and s_ in d) <= 2

        # Restrição: Cada disciplina deve ser alocada uma vez em algum professor/slot permitido
        for m in self.M:
            if m in self.Sm:
                for s in self.Sm[m]:
                    self.model += xsum(
                        self.x[p_, m_, s_] for (p_, m_, s_) in self.x if m_ == m and s_ == s
                    ) == 1

        # Função Objetivo
        alocacoes = xsum(
            self.x[p, m, s]
            for (p, m, s) in self.x
        )

        penalidades = xsum(
            1 - xsum(
                self.x[p, m, s]
                for p in self.P if m in self.Mp[p]
                for s in self.Sm.get(m, [])
                if (p, m, s) in self.x
            )
            for m in self.M
        )

        self.model.objective = alocacoes - 1000 * penalidades
