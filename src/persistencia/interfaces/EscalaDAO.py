from abc import ABC, abstractmethod

# Interface para implementação dos DAOs relativos a Escala
class EscalaDAO(ABC):

    @abstractmethod
    def create(self, escala):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def read(self, id: int):
        pass

    @abstractmethod
    def update(self, id: int, escala):
        pass
