from enum import Enum
from typing import List


# Enumerados auxiliares para a classe Turno
class DiaSemana(Enum):
    SEGUNDA_FEIRA   = 0
    TERCA_FEIRA     = 1
    QUARTA_FEIRA    = 2
    QUINTA_FEIRA    = 3
    SEXTA_FEIRA     = 4
    SABADO          = 5
    DOMINGO         = 6


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

    def getIntId(self):
        return self._diaSemana * 3 + self._horaDia

    # setters
    def appendColaborador(self, id: int):
        if id not in self._colaboradores:
            self._colaboradores.append(id)

    def removeColaborador(self, id: int):
        self._colaboradores = [x for x in self.getColaboradores() if x != id]
