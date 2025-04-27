from ..DAOFactories.DAOFactory import DAOFactory


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
            self._memento_lista = []
            self._curr_memento = None


    def createEscala(self, escala):
        self._escalaDAO.create(escala)

    def deleteEscala(self):
        self._escalaDAO.delete()

    def readEscala(self):
        return self._escalaDAO.read()

    def updateEscala(self, novosDados):
        self._escalaDAO.update(novosDados)

    def getMementoEscala(self):
        return self._escalaDAO.read()

    def createMemento(self, novosDados):
        self._escalaDAO.create(novosDados)
        novo_memento = self._escalaDAO.RAM_EscalaDAOMemento(self._escalaDAO)
        self._memento_lista.append(novo_memento)
        self.setIndexMemento(len(self._memento_lista) - 1)
        return
    
    def setIndexMemento(self, index):
        self._curr_memento = index
        return

    def previousMemento(self):
        if not self._memento_lista:
            return
        if self._curr_memento == 0:
            return
        self._curr_memento -= 1
        self._escalaDAO.setIndexMemento(self._memento_lista[self._curr_memento])
        return
    
    def nextMemento(self):
        if not self._memento_lista:
            return  
        if self._curr_memento == len(self._memento_lista) - 1:
            return
        self._curr_memento += 1
        self._escalaDAO.setIndexMemento(self._memento_lista[self._curr_memento])
        return
