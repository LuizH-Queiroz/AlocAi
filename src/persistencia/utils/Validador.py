MAX_CARACTERES_NOME_COLABORADOR = 100
MAX_CARACTERES_NOME_DISCIPLINA = 100


class Validador:

    def validarDisciplina(self, disciplina) -> bool:
        if not isinstance(disciplina.getId(), int):
            return False

        nome = disciplina.getNome()
        if (
            not isinstance(nome, str)
            or len(nome) > MAX_CARACTERES_NOME_DISCIPLINA
        ):
            return False

        if not isinstance(disciplina.getTurnos(), list):
            return False

        return True

    def validarColaborador(self, colaborador) -> tuple[bool, str]:
        if not isinstance(colaborador.getId(), int):
            return False, "ID do colaborador deve ser um inteiro"

        nome = colaborador.getNome()
        if not isinstance(nome, str):
            return False, "Nome do colaborador deve ser uma string"
        if len(nome) > MAX_CARACTERES_NOME_COLABORADOR:
            return False, f"Nome excede {MAX_CARACTERES_NOME_COLABORADOR} caracteres"

        if not isinstance(colaborador.getTurnos(), list):
            return False, "Turnos devem estar em uma lista"
        
        valores_validos = {str(i) for i in range(0, 15)}  # strings de "1" a "14"
        if not all(item.strip() in valores_validos for item in colaborador.getTurnos()):
            return False, "Turnos devem ser números inteiros entre 0 e 14"

        return True, "Colaborador válido"



    def validarEscala(self, escala) -> bool:
        # if not isinstance(escala.getAtribuicoes()[:][0], list):
        #     return False
    
        return True