from ..utils.Validador import Validador
from ..entidades.Turno import Turno
from typing import List
import copy


class Colaborador:

    def __init__(self, nome: str, id: int, disciplinas, turnos: List[Turno]):
        self._nome          = nome
        self._id            = id
        self._disciplinas   = disciplinas
        self._turnos        = turnos

        self._validar()

    # getters
    def getDisciplinas(self):
        return copy.deepcopy(self._disciplinas)

    def getId(self) -> int:
        return copy.deepcopy(self._id)

    def getNome(self) -> str:
        return copy.deepcopy(self._nome)

    def getTurnos(self) -> List[Turno]:
        return copy.deepcopy(self._turnos)


    # setters
    def setDisciplinas(self, disciplinas):
        self._disciplinas = copy.deepcopy(disciplinas)

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
        resultado = validador.validarColaborador(self)
        if not resultado[0]:
            raise Exception(f'Colaborador {self.getId()} - {self.getNome()} é inválido!\n\nMotivo: {resultado[1]}')
