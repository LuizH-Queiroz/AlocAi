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
            self._colaboradorDAO    = self._daoFactory.getColaboradorDAOCSV()
            

    def createColaborador(self, colaborador):
        try:
            self._colaboradorDAO.create(colaborador)
        except Exception as e:
            print(f'>> Erro ao criar colaborador: {e}')

    def deleteColaborador(self, id: int):
        self._colaboradorDAO.delete(id)

    def readColaborador(self, id: int):
        try:
            return self._colaboradorDAO.read(id)
        except Exception as e:
            print(f'>> Erro ao ler colaborador de id {id}: {e}')

    def readAllColaborador(self):
        return self._colaboradorDAO.readAll()

    def updateColaborador(self, id: int, novosDados):
        try:
            self._colaboradorDAO.update(id, novosDados)
        except Exception as e:
            print(f'>> Erro ao atualizar colaborador de id {id}: {e}')
