from entidades.Colaborador import Colaborador
from entidades.Escala import Escala
from entidades.Turno import DiaSemana, HoraDia
from typing import Dict, Tuple, List


MAX_CARACTERES_NOME_COLABORADOR = 100


class Validador:

    def validarColaborador(self, colaborador: Colaborador) -> bool:
        if not isinstance(colaborador.getId(), int):
            return False

        nome = colaborador.getNome()
        if (
            not isinstance(nome, str)
            or len(nome) > MAX_CARACTERES_NOME_COLABORADOR
        ):
            return False

        if not isinstance(colaborador.getTurnos(), list):
            return False

        return True


    def validarEscala(self, escala: Escala) -> bool:
        if not isinstance(escala.getColaboradores(), List[Colaborador]):
            return False
    
        if not isinstance(
            escala.getTurnos(),
            Dict[Tuple[DiaSemana, HoraDia], List[int]]
        ):
            return False

        return True