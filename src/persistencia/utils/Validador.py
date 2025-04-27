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

    def validarColaborador(self, colaborador) -> bool:
        if not isinstance(colaborador.getId(), int):
            return False

        nome = colaborador.getNome()
        if (
            not isinstance(nome, str)
            or len(nome) > MAX_CARACTERES_NOME_COLABORADOR
        ):
            return False

        if not isinstance(colaborador.getTurnos(), list):
            return False

        return True


    def validarEscala(self, escala) -> bool:
        if not isinstance(escala.getColaboradores(), list):
            return False
    
        return True