from utils.Validador import Validador
from entidades.Turno import Turno
from typing import List
import copy


class Colaborador:

    def __init__(self, nome: str, id: int, turnos: List[Turno]):
        self._nome      = nome
        self._id        = id
        self._turnos    = turnos

        self._validar()

    # getters
    def getId(self) -> int:
        return self._id

    def getNome(self) -> str:
        return self._nome

    def getTurnos(self) -> List[Turno]:
        return self._turnos


    # setters
    def setId(self, id: int):
        temp = copy.deepcopy(self)
        temp._id = id
        temp._validar()

        self.id = id

    def setNome(self, nome: str):
        temp = copy.deepcopy(self)
        temp._nome = nome
        temp._validar()

        self.nome = nome
    
    def setTurnos(self, turnos: List[Turno]):
        self._turnos = copy.deepcopy(turnos)


    # outros metodos (privados)
    def _validar(self):
        validador = Validador()
        if not validador.validarColaborador(self):
            raise Exception(f'Colaborador \"{self}\" é inválido!')
