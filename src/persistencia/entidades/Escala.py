from ..entidades.Turno import DiaSemana, HoraDia
from ..utils.Validador import Validador
from typing import Dict, Tuple, List
import copy


class Escala:

    def __init__(self, atribuicoes):
        self._gerarTurnos()
        self._atribuicoes = atribuicoes # Lista de listas de atribuicoes do tipo
                                        # [idColab, disciplina, horario(int)]

        self._validar()


    def getAtribuicoes(self):
        return copy.deepcopy(self._atribuicoes)

    # getters
    # def getColaboradores(self):
    #     return self._colaboradores

    # def getTurnos(self) -> Dict[Tuple[DiaSemana, HoraDia], List[int]]:
    #     return self._turnos


    # outros metodos (privados)
    # def _atribuirColaboradorTurno(self):
    #     for colaborador in self._colaboradores:
    #         for turno in colaborador.getTurnos():
    #             self._turnos[
    #                 (turno.getDiaSemana(), turno.getHoraDia())
    #             ].append(colaborador.getId())

    # def _gerarTurnos(self):
    #     self._turnos = {
    #         (dia, hora): []
    #         for dia in DiaSemana
    #         for hora in HoraDia
    #     }
    
    def _validar(self):
        validador = Validador()
        if not validador.validarEscala(self):
            raise Exception(f'Escala \"{self}\" é inválida!')
