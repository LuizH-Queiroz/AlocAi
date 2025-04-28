from ..entidades.Colaborador import Colaborador
from ..interfaces.ColaboradorDAO import ColaboradorDAO
from typing import List
import csv


FILEPATH = 'solvers/School_timetabling_main/Data/VALIDAÇÃO/'


class CSV_ColaboradorDAO(ColaboradorDAO):
    _instancia      = None
    _inicializado   = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia  = super().__new__(cls)  # Cria uma unica instancia
        return cls._instancia
    
    def __init__(self):
        if not self._inicializado:
            self._inicializado = True

            self._file      = FILEPATH + 'professores.csv'

    def create(self, colaborador: Colaborador):
        with open(self._file, mode='r', newline='') as file:
            colaboradores = list(csv.reader(file))

        # Procura se já existe o ID
        found = False
        for i in range(len(colaboradores)):
            if colaboradores[i][0] == str(colaborador.getId()):  # <-- pega só o ID da linha
                found = True
                break

        if found:
            raise Exception(
                f'Já existe colaborador com id {colaborador.getId()}'
            )

        with open(self._file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self._colaboradorToList(colaborador))


    def delete(self, id: int):
        with open(self._file, mode='r', newline='') as file:
            colaboradores = list(csv.reader(file))
        
        colaboradores = [
            colab for colab in colaboradores
            if colab and colab[0] != str(id)
        ]

        with open(self._file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(colaboradores)

    def read(self, id: int) -> Colaborador:
        with open(self._file, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # pula o cabeçalho

            for row in reader:
                colab_id = int(row[0])
                if colab_id == id:
                    nome = row[1]
                    disciplinas = row[2].split(',')  # separa as disciplinas
                    turnos = row[3].split(',')  # separa e transforma em int

                    return Colaborador(nome, colab_id, disciplinas, turnos)

        raise Exception(f'Não existe colaborador com id {id}')


    def readAll(self) -> List[Colaborador]:
        colaboradores = []

        with open(self._file, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # pula o cabeçalho

            for row in reader:
                colab_id = int(row[0])
                nome = row[1]
                disciplinas = row[2].split(',')  # disciplinas já em lista
                turnos = row[3].split(',')  # slots como lista de strings

                colaborador = Colaborador(nome, colab_id, disciplinas, turnos)
                colaboradores.append(colaborador)

        return colaboradores

    def update(self, id: int, colaborador: Colaborador):

        # Lendo todos os colaboradores
        with open(self._file, mode='r', newline='') as file:
            colaboradores = list(csv.reader(file))
        
        # Procura e atualiza o colaborador
        found = False
        for i in range(len(colaboradores)):
            if colaboradores[i][0] == str(id):
                found = True
                colaboradores[i] = self._colaboradorToList(colaborador)
                break

        # Excecao de colaborador nao encontrado
        if not found:
            raise Exception(f'Não existe colaborador com id {id}')

        # Reescrevendo o arquivo
        with open(self._file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(colaboradores)


    # Metodos privados
    def _colaboradorToList(self, colaborador):
        disciplinasStr = ','.join(d.strip() for d in colaborador.getDisciplinas())
        turnosStr = ','.join(t.strip() for t in colaborador.getTurnos())

        return [
            colaborador.getId(),
            colaborador.getNome(),
            disciplinasStr,
            turnosStr
        ]