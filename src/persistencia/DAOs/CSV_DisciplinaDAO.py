from ..entidades.Disciplina import Disciplina
from ..interfaces.DisciplinaDAO import DisciplinaDAO
from typing import List
import csv


FILEPATH = 'solvers/School_timetabling_main/Data/VALIDAÇÃO/'


class CSV_DisciplinaDAO(DisciplinaDAO):
    _instancia      = None
    _inicializado   = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia  = super().__new__(cls)  # Cria uma unica instancia
        return cls._instancia
    
    def __init__(self):
        if not self._inicializado:
            self._inicializado = True

            self._file      = FILEPATH + 'disciplinas.csv'

    def create(self, disciplina):
        # Lendo todas as disciplinas, pulando o cabeçalho
        with open(self._file, mode='r', newline='') as file:
            disciplinas = list(csv.reader(file))

        # Pulando o cabeçalho
        disciplinas = disciplinas[1:]  # Ignora a primeira linha que é o cabeçalho
        
        # Procura e atualiza a disciplina
        found = False
        for i in range(len(disciplinas)):
            if int(disciplinas[i][0]) == disciplina.getId():  # Comparando IDs
                found = True
                break

        # Excecao de disciplina ja existente
        if found:
            raise Exception(f'Já existe disciplina com id {disciplina.getId()}')

        # Escrevendo no arquivo
        with open(self._file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self._disciplinaToList(disciplina))

    def delete(self, id: int):
        # Lendo todas as disciplinas
        with open(self._file, mode='r', newline='') as file:
            disciplinas = list(csv.reader(file))

        # Filtra as disciplinas, excluindo a disciplina com o id fornecido
        disciplinas = [
            discip for discip in disciplinas
            if discip and discip[0] != str(id)  # Corrigido: str(id) e não srt(id)
        ]

        # Reescrevendo o arquivo
        with open(self._file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(disciplinas)

    def read(self, id: int):
        # Lendo todas as disciplinas
        with open(self._file, mode='r', newline='') as file:
            disciplinas = list(csv.reader(file))

        # Ignora o cabeçalho (primeira linha)
        disciplinas = disciplinas[1:]

        # Iterando sobre as disciplinas e verificando o ID
        for discip in disciplinas:
            # O id está na primeira posição (disciplinas[i][0])
            if int(discip[0]) == id:
                # Criando o objeto Disciplina a partir da linha do CSV
                nome = discip[1]
                turnos = discip[2].split(',')  # Convertendo os turnos para objetos Turno
                return Disciplina(nome, int(discip[0]), turnos)

        raise Exception(f'Não existe disciplina com id {id}')

    def readAll(self):
        # Lendo todas as disciplinas
        with open(self._file, mode='r', newline='') as file:
            disciplinas = list(csv.reader(file))

        # Ignora o cabeçalho (primeira linha)
        disciplinas = disciplinas[1:]

        # Convertendo cada linha em um objeto Disciplina
        disciplinas_objetos = []
        for discip in disciplinas:
            nome = discip[1]
            turnos = [int(t) for t in discip[2].strip('"').split(',')]  # Convertendo os turnos para inteiros
            disciplina_objeto = Disciplina(nome, int(discip[0]), turnos)
            disciplinas_objetos.append(disciplina_objeto)

        return disciplinas_objetos

    def update(self, id: int, disciplina):

        # Lendo todas as disciplinas
        with open(self._file, mode='r', newline='') as file:
            disciplinas = list(csv.reader(file))
        
        # Procura e atualiza a disciplina
        found = False
        for i in range(len(disciplinas)):
            if disciplinas[i][0] == str(id):
                found = True
                disciplinas[i] = self._disciplinaToList(disciplina)
                break

        # Excecao de disciplina nao encontrada
        if not found:
            raise Exception(f'Não existe disciplina com id {id}')

        # Reescrevendo o arquivo
        with open(self._file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(disciplinas)


    # Metodos privados
    def _disciplinaToList(self, disciplina):
        # Converte os turnos para uma string com IDs separados por vírgula
        turnosStr = ','.join(t.strip() for t in disciplina.getTurnos())  # Aqui, t é um objeto Turno
        
        return [
            disciplina.getId(),
            disciplina.getNome(),
            turnosStr 
        ]

