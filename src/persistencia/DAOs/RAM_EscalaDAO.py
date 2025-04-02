from entidades.Escala import Escala
from interfaces.EscalaDAO import EscalaDAO
from typing import List


class RAM_EscalaDAO(EscalaDAO):
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)  # Cria uma unica instancia
        return cls._instancia

    def create(self, escala: Escala):
        pass

    def delete(self, id: int):
        pass

    def read(self, id: int) -> Escala:
        pass

    def readAll(self) -> List[Escala]:
        pass

    def update(self, id: int, escala: Escala):
        pass
