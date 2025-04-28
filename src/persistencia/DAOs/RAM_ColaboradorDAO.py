from ..entidades.Colaborador import Colaborador
from ..interfaces.ColaboradorDAO import ColaboradorDAO
from typing import List
import copy


class RAM_ColaboradorDAO(ColaboradorDAO):
    _instancia      = None
    _inicializado   = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia      = super().__new__(cls)  # Cria uma unica instancia
        return cls._instancia
    
    def __init__(self):
        if not self._inicializado:
            self._inicializado = True

            self._colaboradores = []

    def create(self, colaborador: Colaborador):
        for colab in self._colaboradores:
            if colab.getId() == colaborador.getId():
                raise Exception(f'Já existe colabordor com id {colab.getId()}!')

        self._colaboradores.append(copy.deepcopy(colaborador))

    def delete(self, id: int):
        self._colaboradores = [
            colaborador for colaborador in self._colaboradores
            if colaborador.getId() != id
        ]

    def read(self, id: int) -> Colaborador:
        for colab in self._colaboradores:
            if colab.getId() == id:
                return copy.deepcopy(colab)

        raise Exception(f'Não existe colaborador com id {id}')

    def readAll(self) -> List[Colaborador]:
        return copy.deepcopy(self._colaboradores)

    def update(self, id: int, colaborador: Colaborador):
        for colab in self._colaboradores:
            if colab.getId() == id:
                self._colaboradores.remove(colab)
                self._colaboradores.append(copy.deepcopy(colaborador))
                return

        raise Exception(f'Não existe colaborador com id {id}')
