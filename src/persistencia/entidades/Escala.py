from entidades.Turno import DiaSemana, HoraDia
from entidades.Colaborador import Colaborador
from utils.Validador import Validador
from typing import Dict, Tuple, List


class Escala:

    def __init__(self, colaboradores: List[Colaborador]):
        self._gerarTurnos()
        self._colaboradores = colaboradores
        self._atribuirColaboradorTurno()

        self._validar()
    

    # getters
    def getColaboradores(self) -> List[Colaborador]:
        return self._colaboradores

    def getTurnos(self) -> Dict[Tuple[DiaSemana, HoraDia], List[int]]:
        return self._turnos


    # outros metodos (privados)
    def _atribuirColaboradorTurno(self):
        for colaborador in self._colaboradores:
            for turno in colaborador.getTurnos():
                self._turnos[
                    (turno.getDiaSemana(), turno.getHoraDia())
                ].append(colaborador.getId())

    def _gerarTurnos(self):
        self._turnos = {
            (dia, hora): []
            for dia in DiaSemana
            for hora in HoraDia
        }
    
    def _validar(self):
        validador = Validador()
        if not validador.validarEscala(self):
            raise Exception(f'Escala \"{self}\" é inválida!')
