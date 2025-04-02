from DAOs.RAM_ColaboradorDAO import RAM_ColaboradorDAO
from DAOs.RAM_EscalaDAO import RAM_EscalaDAO

# Factory para instanciação das DAOs:
# - EscalaDAO
# - ColaboradorDAO
class DAOFactory:

    def getColaboradorDAO(self):
        return RAM_ColaboradorDAO()

    def getEscalaDAO(self):
        return RAM_EscalaDAO()
