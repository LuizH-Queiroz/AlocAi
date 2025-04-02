from entidades.Colaborador import Colaborador
from interfaces.ColaboradorDAO import ColaboradorDAO
from typing import List


class RAM_ColaboradorDAO(ColaboradorDAO):
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)  # Cria uma unica instancia
        return cls._instancia

    def create(self, colaborador: Colaborador):
        pass

    def delete(self, id: int):
        pass

    def read(self, id: int) -> Colaborador:
        pass

    def readAll(self) -> List[Colaborador]:
        pass

    def update(self, id: int, colaborador: Colaborador):
        pass
