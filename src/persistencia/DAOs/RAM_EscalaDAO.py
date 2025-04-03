from entidades.Escala import Escala
from interfaces.EscalaDAO import EscalaDAO
from typing import List
import copy


class RAM_EscalaDAO(EscalaDAO):
    _instancia = None
    _inicializado   = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)  # Cria uma unica instancia
        return cls._instancia

    def __init__(self):
        if not self._inicializado:
            self._inicializado = True

            self._escala = None

    def create(self, escala: Escala):
        self._escala = copy.deepcopy(escala)

    def delete(self):
        self._escala = None

    def read(self) -> Escala:
        if self._escala:
            return copy.deepcopy(self._escala)

        raise Exception(f'Ainda não há escala!')

    def update(self, escala: Escala):
        self._escala = copy.deepcopy(escala)
