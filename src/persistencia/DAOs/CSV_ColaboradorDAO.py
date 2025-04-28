from ..entidades.Colaborador import Colaborador
from ..interfaces.ColaboradorDAO import ColaboradorDAO
from typing import List
import csv


FILEPATH = '../../solvers/School_timetabling_main/Data/VALIDAÇÃO/'


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
        # Lendo todos os colaboradores
        with open(self._file, mode='r', newline='') as file:
            colaboradores = list(csv.reader(file))
        
        # Procura e atualiza o colaborador
        found = False
        for i in range(len(colaboradores)):
            if colaboradores[i] == str(colaborador.getId()):
                found = True
                break

        # Excecao de colaborador nao encontrado
        if found:
            raise Exception(
                f'Já existe colaborador com id {colaborador.getId()}'
            )

        with open(self._file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self._colaboradorToList(colaborador))

    def delete(self, id: int):

        # Lendo todos os colaboradores
        with open(self._file, mode='r', newline='') as file:
            colaboradores = list(csv.reader(file))
        
        colaboradores = [
            colab for colab in colaboradores
            if colab.getId() != id
        ]

        # Reescrevendo o arquivo
        with open(self._file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(colaboradores)

    def read(self, id: int) -> Colaborador:
        # Lendo todos os colaboradores
        with open(self._file, mode='r', newline='') as file:
            colaboradores = list(csv.reader(file))

        for colab in colaboradores:
            if colab.getId() == id:
                return colab

        raise Exception(f'Não existe colaborador com id {id}')

    def readAll(self) -> List[Colaborador]:
        # Lendo todos os colaboradores
        with open(self._file, mode='r', newline='') as file:
            colaboradores = list(csv.reader(file))
        
        return colaboradores

    def update(self, id: int, colaborador: Colaborador):

        # Lendo todos os colaboradores
        with open(self._file, mode='r', newline='') as file:
            colaboradores = list(csv.reader(file))
        
        # Procura e atualiza o colaborador
        found = False
        for i in range(len(colaboradores)):
            if colaboradores[i] == str(id):
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

        disciplinasStr = '\"'
        for discip in colaborador.getDisciplinas():
            disciplinasStr += discip + ','
        disciplinasStr = disciplinasStr[:-1]
        disciplinasStr += '\"'

        turnosStr = '\"'
        for t in colaborador.getTurnos():
            turnosStr += str(t.getIntId()) + ','
        turnosStr = turnosStr[:-1]
        turnosStr += '\"'

        return [
            colaborador.getId(),
            colaborador.getNome(),
            disciplinasStr,
            turnosStr
        ]
