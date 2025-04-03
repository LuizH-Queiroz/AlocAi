from abc import ABC, abstractmethod


# Interface para implementação dos DAOs relativos a Colaborador
class ColaboradorDAO(ABC):

    @abstractmethod
    def create(self, colaborador):
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
    def update(self, id: int, colaborador):
        pass
