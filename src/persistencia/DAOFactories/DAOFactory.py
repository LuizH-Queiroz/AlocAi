from ..DAOs.RAM_ColaboradorDAO import RAM_ColaboradorDAO
from ..DAOs.RAM_EscalaDAO import RAM_EscalaDAO
from ..DAOs.RAM_DisciplinaDAO import RAM_DisciplinaDAO
from ..DAOs.CSV_ColaboradorDAO import CSV_ColaboradorDAO
from ..DAOs.CSV_DisciplinaDAO import CSV_DisciplinaDAO
from ..DAOs.CSV_EscalaDAO import CSV_EscalaDAO

# Factory para instanciação das DAOs:
# - EscalaDAO
# - ColaboradorDAO
class DAOFactory:

    def getColaboradorDAO(self):
        return RAM_ColaboradorDAO()

    def getEscalaDAO(self):
        return RAM_EscalaDAO()

    def getDisciplinaDAO(self):
        return RAM_DisciplinaDAO()
    
    def getColaboradorDAOCSV(self):
        return CSV_ColaboradorDAO()

    def getEscalaDAOCSV(self):
        return CSV_EscalaDAO()
    
    def getDisciplinaDAOCSV(self):
        return CSV_DisciplinaDAO()
