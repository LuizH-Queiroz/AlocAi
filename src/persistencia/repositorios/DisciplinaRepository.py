from ..DAOFactories.DAOFactory import DAOFactory


class DisciplinaRepository:
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
            self._disciplinaDAO    = self._daoFactory.getDisciplinaDAOCSV()
            

    def createDisciplina(self, disciplina):
        self._disciplinaDAO.create(disciplina)

    def deleteDisciplina(self, id: int):
        self. _disciplinaDAO.delete(id)

    def readDisciplina(self, id: int):
        return self. _disciplinaDAO.read(id)

    def readAllDisciplina(self):
        return self. _disciplinaDAO.readAll()

    def updateDisciplina(self, id: int, novosDados):
        self. _disciplinaDAO.update(id, novosDados)
