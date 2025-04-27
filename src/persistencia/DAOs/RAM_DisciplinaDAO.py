from ..entidades.Disciplina import Disciplina
from ..interfaces.DisciplinaDAO import DisciplinaDAO
from typing import List
import copy

class RAM_DisciplinaDAO(DisciplinaDAO):
    _instancia      = None
    _inicializado   = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia      = super().__new__(cls)  # Cria uma unica instancia
        return cls._instancia
    
    def __init__(self):
        if not self._inicializado:
            self._inicializado = True

            self._disciplinas = []

    def create(self, disciplina: Disciplina):
        for disc in self._disciplinas:
            if disc.getId() == disciplina.getId():
                raise Exception(f'Já existe disciplina com id {disciplina.getId()}!')

        self._disciplinas.append(copy.deepcopy(disciplina))

    def delete(self, id: int):
        self._disciplinas = [
            disciplina for disciplina in self._disciplinas
            if disciplina.getId() != id
        ]

    def read(self, id: int) -> Disciplina:
        for disc in self._disciplinas:
            if disc.getId() == id:
                return copy.deepcopy(disc)

        raise Exception(f'Não existe disciplina com id {id}')

    def readAll(self) -> List[Disciplina]:
        return copy.deepcopy(self._disciplinas)

    def update(self, id: int, disciplina: Disciplina):
        for disc in self._disciplinas:
            if disc.getId() == id:
                self._disciplinas.remove(disc)
                self._disciplinas.append(copy.deepcopy(disciplina))
                return

        raise Exception(f'Não existe disciplina com id {id}')


    # Metodos relativos ao Memento
    def getMemento(self):
        return copy.deepcopy(self.RAM_DisciplinaDAOMemento(self))

    def setMemento(self, memento):
        self._disciplinas = copy.deepcopy(memento)


    ############################################################################
    
    # Subclasse do Memento de RAM_ColaboradorDAO
    class RAM_DisciplinaDAOMemento:

        def __init__(self, disciplinaDAO):
            self._disciplinas = copy.deepcopy(disciplinaDAO._disciplinas)
