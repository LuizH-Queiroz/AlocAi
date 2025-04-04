# src/ui/UIInterface.py
from abc import ABC, abstractmethod


class UIInterface(ABC):
    @abstractmethod
    def show(self):
        pass
