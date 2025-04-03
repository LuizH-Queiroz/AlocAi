from DAOFactories.DAOFactory import DAOFactory
from entidades.Escala import Escala
from typing import List


class EscalaRepository:
    _instancia      = None
    _inicializado   = False

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)  # Cria uma unica instancia

        return cls._instancia

    def __init__(self):
        if not self._inicializado:
            self._inicializado = True

            self._daoFactory = DAOFactory()
            self._escalaDAO = self._daoFactory.getEscalaDAO()


    def createEscala(self, escala: Escala):
        self._escalaDAO.create(escala)

    def deleteEscala(self):
        self._escalaDAO.delete()

    def readEscala(self) -> Escala:
        return self._escalaDAO.read()

    def updateEscala(self, novosDados: Escala):
        self._escalaDAO.update(novosDados)
