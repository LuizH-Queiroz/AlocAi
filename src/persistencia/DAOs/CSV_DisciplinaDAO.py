from ..entidades.Disciplina import Disciplina
from ..interfaces.DisciplinaDAO import DisciplinaDAO
from typing import List
import csv


FILEPATH = 'solvers/School_timetabling_main/Data/VALIDAÇÃO/'


class CSV_DisciplinaDAO(DisciplinaDAO):
    _instancia      = None
    _inicializado   = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia  = super().__new__(cls)  # Cria uma unica instancia
        return cls._instancia
    
    def __init__(self):
        if not self._inicializado:
            self._inicializado = True

            self._file      = FILEPATH + 'disciplinas.csv'

    def create(self, disciplina):
        # Lendo todas as disciplinas
        with open(self._file, mode='r', newline='') as file:
            disciplinas = list(csv.reader(file))
        
        # Procura e atualiza a disciplina
        found = False
        for i in range(len(disciplinas)):
            if disciplinas[i] == str(disciplina.getId()):
                found = True
                break

        # Excecao de disciplina nao encontrada
        if found:
            raise Exception(
                f'Já existe disciplina com id {disciplina.getId()}'
            )

        with open(self._file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self._disciplinaToList(disciplina))

    def delete(self, id: int):

        # Lendo todos as disciplinas
        with open(self._file, mode='r', newline='') as file:
            disciplinas = list(csv.reader(file))
        
        disciplinas = [
            discip for discip in disciplinas
            if discip.getId() != id
        ]

        # Reescrevendo o arquivo
        with open(self._file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(disciplinas)

    def read(self, id: int):
        # Lendo todas as disciplinas
        with open(self._file, mode='r', newline='') as file:
            disciplinas = list(csv.reader(file))

        for discip in disciplinas:
            if discip.getId() == id:
                return discip

        raise Exception(f'Não existe disciplina com id {id}')

    def readAll(self):
        # Lendo todas as disciplinas
        with open(self._file, mode='r', newline='') as file:
            disciplinas = list(csv.reader(file))
        
        return disciplinas

    def update(self, id: int, disciplina):

        # Lendo todas as disciplinas
        with open(self._file, mode='r', newline='') as file:
            disciplinas = list(csv.reader(file))
        
        # Procura e atualiza a disciplina
        found = False
        for i in range(len(disciplinas)):
            if disciplinas[i] == str(id):
                found = True
                disciplinas[i] = self._colaboradorToList(disciplina)
                break

        # Excecao de disciplina nao encontrada
        if not found:
            raise Exception(f'Não existe disciplina com id {id}')

        # Reescrevendo o arquivo
        with open(self._file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(disciplinas)


    # Metodos privados
    def _disciplinaToList(self, disciplina):

        turnosStr = '\"'
        for t in disciplina.getTurnos():
            turnosStr += str(t.getIntId()) + ','
        turnosStr = turnosStr[:-1]
        turnosStr += '\"'

        return [
            disciplina.getId(),
            disciplina.getNome(),
            turnosStr
        ]
