from ..DAOFactories.DAOFactory import DAOFactory
import os
import re


FILEPATH = 'solvers/School_timetabling_main/Data/VALIDAÇÃO/'


class EscalaRepository:
    _instancia = None
    _inicializado = False

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        if not self._inicializado:
            self._inicializado = True

            self._daoFactory = DAOFactory()
            self._escalaDAO = self._daoFactory.getEscalaDAOCSV()
            self._memento_lista = []
            self._curr_memento = -1

            self._carregarUltimaEscalaSeExistir()

    def _carregarUltimaEscalaSeExistir(self):
        try:
            arquivos = [f for f in os.listdir(FILEPATH) if f.startswith("escala") and f.endswith(".csv")]

            if not arquivos:
                self._escalaDAO.set_file_count(0)
                return

            # Extrai os números dos arquivos e encontra o maior
            numeros = [int(re.findall(r'\d+', f)[0]) for f in arquivos]
            maior_numero = max(numeros)

            # Seta o contador no DAO
            self._escalaDAO.set_file_count(maior_numero)

            # Seta o caminho do arquivo de maior número como arquivo atual
            ultimo_arquivo = f"escala{maior_numero}.csv"
            self._escalaDAO._file = os.path.join(FILEPATH, ultimo_arquivo)

            # Cria memento com esse arquivo
            ultimo_memento = self._escalaDAO.CSV_EscalaDAOMemento(self._escalaDAO)
            self._memento_lista.append(ultimo_memento)
            self._curr_memento = 0

        except Exception as e:
            print(f">> Erro ao carregar escala mais recente: {e}")

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
        novo_memento = self._escalaDAO.CSV_EscalaDAOMemento(self._escalaDAO)
        self._memento_lista.append(novo_memento)
        self.setIndexMemento(len(self._memento_lista) - 1)

    def setIndexMemento(self, index):
        self._curr_memento = index
        self._escalaDAO.setMemento(self._memento_lista[self._curr_memento])

    def previousMemento(self):
        if not self._memento_lista or self._curr_memento == 0:
            return
        self._curr_memento -= 1
        self.setIndexMemento(self._curr_memento)

    def nextMemento(self):
        if not self._memento_lista or self._curr_memento == len(self._memento_lista) - 1:
            return
        self._curr_memento += 1
        self.setIndexMemento(self._curr_memento)
