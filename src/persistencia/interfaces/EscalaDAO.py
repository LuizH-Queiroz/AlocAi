from abc import ABC, abstractmethod
from entidades.Escala import Escala
from typing import List

# Interface para implementação dos DAOs relativos a Escala
class EscalaDAO(ABC):

    @abstractmethod
    def create(self, escala: Escala):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def read(self, id: int) -> Escala:
        pass

    @abstractmethod
    def update(self, id: int, escala: Escala):
        pass
