from DAOFactories.DAOFactory import DAOFactory
from entidades.Colaborador import Colaborador
from typing import List


class ColaboradorRepository:
    _instancia      = None
    _colaboradorDAO = None
    _daoFactory     = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)  # Cria uma unica instancia

            cls._daoFactory = DAOFactory()
            cls._colaboradorDAO = cls._daoFactory.getColaboradorDAO()
        return cls._instancia

    def createColaborador(self, idColaborador: int, colaborador: Colaborador):
        pass

    def deleteColaborador(self, id: int):
        pass

    def readColaborador(self, id: int) -> Colaborador:
        pass

    def readAllColaborador(self) -> List[Colaborador]:
        pass

    def updateColaborador(self, id: int, novosDados: Colaborador):
        pass
