# src/ui/UIFactory.py
from .MainWindowUI import MainWindowUI
from .EscalaUI import EscalaUI
from .CadastroColaboradorUI import CadastroColaboradorUI
from .RelatorioUI import RelatorioUI
from .DisciplinaUI import DisciplinaUI

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
    
    @staticmethod
    def generateDisciplinaUI():
        return DisciplinaUI()
    
    @staticmethod
    def generateRelatorioUI():
        return RelatorioUI()
