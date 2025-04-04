from ..repositorios.ColaboradorRepository import ColaboradorRepository
from ..repositorios.EscalaRepository import EscalaRepository


class PersistenciaFactory:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)  # Cria uma unica instancia
        return cls._instancia

    def getColaboradorRepository(self):
        return ColaboradorRepository()

    def getEscalaRepository(self):
        return EscalaRepository()
