from ..DAOFactories.DAOFactory import DAOFactory


class ColaboradorRepository:
    _instancia      = None
    _inicializado   = False

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)  # Cria uma unica instancia

        return cls._instancia

    def __init__(self):
        if not self._inicializado:
            self._inicializado      = True

            self._daoFactory        = DAOFactory()
            self._colaboradorDAO    = self._daoFactory.getColaboradorDAO()
            

    def createColaborador(self, colaborador):
        self._colaboradorDAO.create(colaborador)

    def deleteColaborador(self, id: int):
        self._colaboradorDAO.delete(id)

    def readColaborador(self, id: int):
        return self._colaboradorDAO.read(id)

    def readAllColaborador(self):
        return self._colaboradorDAO.readAll()

    def updateColaborador(self, id: int, novosDados):
        self._colaboradorDAO.update(id, novosDados)
