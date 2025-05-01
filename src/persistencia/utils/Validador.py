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

        return True, "Colaborador válido"



    def validarEscala(self, escala) -> bool:
        # if not isinstance(escala.getAtribuicoes()[:][0], list):
        #     return False
    
        return True