from abc import ABC, abstractmethod
from entidades.Colaborador import Colaborador
from typing import List

# Interface para implementação dos DAOs relativos a Colaborador
class ColaboradorDAO(ABC):

    @abstractmethod
    def create(self, colaborador: Colaborador):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def read(self, id: int) -> Colaborador:
        pass

    @abstractmethod
    def readAll(self) -> List[Colaborador]:
        pass

    @abstractmethod
    def update(self, id: int, colaborador: Colaborador):
        pass
