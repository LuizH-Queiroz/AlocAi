from enum import Enum
from typing import List


# Enumerados auxiliares para a classe Turno
class DiaSemana(Enum):
    DOMINGO         = 1
    SEGUNDA_FEIRA   = 2
    TERCA_FEIRA     = 3
    QUARTA_FEIRA    = 4
    QUINTA_FEIRA    = 5
    SEXTA_FEIRA     = 6
    SABADO          = 7


class HoraDia(Enum):
    MANHA   = 1
    TARDE   = 2
    NOITE   = 3
################################################################################


class Turno:

    def __init__(self, dia: DiaSemana, hora: HoraDia, colaboradores: List[int]):
        self._diaSemana     = dia
        self._horaDia       = hora
        self._colaboradores  = colaboradores # colaboradores sao identificados
                                             # pelos seus respectivos id's
    
    # getters
    def getDiaSemana(self) -> DiaSemana:
        return self._diaSemana

    def getHoraDia(self) -> HoraDia:
        return self._horaDia

    def getColaboradores(self) -> List[int]:
        return self._colaboradores


    # setters
    def appendColaborador(self, id: int):
        if id not in self._colaboradores:
            self._colaboradores.append(id)

    def removeColaborador(self, id: int):
        self._colaboradores = [x for x in self.getColaboradores() if x != id]
