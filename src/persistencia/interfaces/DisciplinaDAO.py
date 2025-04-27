from abc import ABC, abstractmethod


# Interface para implementação dos DAOs relativos a Colaborador
class DisciplinaDAO(ABC):

    @abstractmethod
    def create(self, disciplina):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def read(self, id: int):
        pass

    @abstractmethod
    def readAll(self):
        pass

    @abstractmethod
    def update(self, id: int, disciplina):
        pass
