from gurobipy import Model, GRB, quicksum

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
        solucao = ""
        solucao += "\nSOLUÇÃO FINAL\n" + "-" * 30

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
        self.model.setParam('TimeLimit', 3600)
        self.model.optimize()

        if self.model.status == GRB.INFEASIBLE:
            return False

        print(f'Status da solução = {self.model.status}')
        print(f"Solution value = {self.model.objVal:.2f}\n")
        print("Solution:")
        for v in self.model.getVars():
            if v.x > 0.00001:
                print(f"{v.varName} = {v.x:.2f}")
                if v.varName.startswith('x'):
                    self.solution.append(v.varName)

        self.save_solution()
        return True

    def create_model(self):
        self.model = Model()

        # Criando as variáveis binárias
        self.x = {
            (p, m, s): self.model.addVar(vtype=GRB.BINARY, name=f"x_{p}_{m}_{s}")
            for p in self.P
            for m in self.Mp[p]
            for s in self.Sp[p]
            if m in self.Sm and s in self.Sm.get(m, [])
        }

        self.model.update()

        # Adicionando restrições para que cada professor ocupe no máximo um slot por vez
        for p in self.P:
            for s in self.Sp[p]:
                self.model.addConstr(
                    quicksum(self.x[p_, m, s_] for (p_, m, s_) in self.x if p_ == p and s_ == s) <= 1
                )

        # Adicionando restrições para que cada professor tenha no máximo 2 disciplinas por dia
        for p in self.P:
            for d in self.Sd:
                self.model.addConstr(
                    quicksum(self.x[p_, m, s_] for (p_, m, s_) in self.x if p_ == p and s_ in d) <= 2
                )

        # Garantindo que cada disciplina tenha no máximo um professor por slot permitido
        for m in self.M:
            if m in self.Sm:
                for s in self.Sm[m]:
                    self.model.addConstr(
                        quicksum(self.x[p_, m_, s_] for (p_, m_, s_) in self.x if m_ == m and s_ == s) == 1
                    )

        # Ajustando a função objetivo para considerar a alocação das disciplinas
        self.model.setObjective(
            # Maximizamos o total de alocações viáveis (termo positivo)...
            quicksum(
                self.x[p, m, s]
                for p in self.P
                for m in self.Mp[p]
                for s in self.Sp[p]
                if m in self.Sm and s in self.Sm[m] and (p, m, s) in self.x
            )
            # ... e penalizamos fortemente disciplinas que não foram alocadas em nenhum slot permitido
            - 1000 * quicksum(
                1 - quicksum(
                    self.x[p, m, s]
                    for p in self.P if m in self.Mp[p]
                    for s in self.Sm.get(m, [])
                    if (p, m, s) in self.x
                )
                for m in self.M
            ),
            GRB.MAXIMIZE
        )




