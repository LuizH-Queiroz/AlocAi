from ..entidades.Escala import Escala
from ..interfaces.EscalaDAO import EscalaDAO
import os
import copy
import csv


FILEPATH = 'solvers/School_timetabling_main/Data/VALIDAÇÃO/'


class CSV_EscalaDAO(EscalaDAO):
    _instancia      = None
    _inicializado   = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia  = super().__new__(cls)  # Cria uma unica instancia
        return cls._instancia
    
    def __init__(self):
        if not self._inicializado:
            self._inicializado = True

            self._filecount = 0

    def create(self, escala: Escala):
        self._setNextFile()
        print(escala)
        with open(self._file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(escala.getAtribuicoes())

    def delete(self):

        try:
            os.remove(self._file)
        except Exception as e:
            print(f">> Erro ao deletar arquivo {self._file}: {e}")


    def read(self):
        with open(self._file, mode='r', newline='') as file:
            escala = list(csv.reader(file))

        return escala


    def update(self, id: int, escala: Escala):
        self.create(escala)


    # Metodos privados
    def _setNextFile(self):
        self._filecount += 1
        filename  = f'escala{self._filecount}.csv'
        self._file      = FILEPATH + filename

        try:
            with open(self._file, mode='w', newline='') as file:
                pass
        except Exception as e:
            print(f'>> Erro ao abrir arquivo {self._file}: {e}')
    
    def set_file_count(self, count):
        self._filecount = count


    # Metodos relativos ao Memento
    def getMemento(self):
        return copy.deepcopy(self.CSV_EscalaDAOMemento(self))

    def setMemento(self, memento):

        try:
            with open(memento._escala, mode='r') as file:
                pass
        except Exception as e:
            msg =   f'>> Erro ao abrir arquivo {memento._escala}: {e}\n'
            msg +=  f'>> Escala possivelmente foi deletada anteriormente\n'
            raise Exception(msg)

        self._file = memento._escala


    ############################################################################
    
    # Subclasse do Memento de RAM_EscalaDAO
    class CSV_EscalaDAOMemento:

        def __init__(self, escalaDAO):
            self._escala = copy.deepcopy(escalaDAO._file)
