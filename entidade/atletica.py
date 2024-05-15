from entidade.aluno import Aluno


class Atletica():
    def __init__(self, curso, nome):
        self.__curso = curso
        self.__nome = nome
        self.__alunos = []


    @property
    def curso(self):
        return self.__curso

    @property
    def nome(self):
        return self.__nome

    @property
    def alunos(self):
        return self.__alunos

    def adc_aluno(self, aluno):
        # aluno do mesmo curso 
        if isinstance(aluno, Aluno):
            self.__alunos.append(aluno)

    def remove_aluno(self, aluno):
        # verificar se esta na lista de alunos 
        self.__alunos.remove(aluno)
