from DAOFactories.DAOFactory import DAOFactory
from entidades.Escala import Escala
from typing import List


class EscalaRepository:
    _instancia      = None
    _escalaDAO      = None
    _daoFactory     = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)  # Cria uma unica instancia

            cls._daoFactory = DAOFactory()
            cls._escalaDAO = cls._daoFactory.getEscalaDAO()
        return cls._instancia

    def createEscala(self, idEscala: int, escala: Escala):
        pass

    def deleteEscala(self, id: int):
        pass

    def readEscala(self, id: int) -> Escala:
        pass

    def readAllEscala(self) -> List[Escala]:
        pass

    def updateEscala(self, id: int, novosDados: Escala):
        pass
