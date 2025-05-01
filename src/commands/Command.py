from abc import ABC, abstractmethod

from sistema.sistema import Sistema


class Command(ABC):
    
    @abstractmethod
    def execute(self, sistema: Sistema):
        pass