# src/ui/UIFactory.py
from .MainWindowUI import MainWindowUI
from .EscalaUI import EscalaUI
from .CadastroColaboradorUI import CadastroColaboradorUI

class UIFactory:
    @staticmethod
    def generateMainUI():
        return MainWindowUI()
    
    @staticmethod
    def generateEscalaUI():
        return EscalaUI()
    
    @staticmethod
    def generateCCUI():
        return CadastroColaboradorUI()
