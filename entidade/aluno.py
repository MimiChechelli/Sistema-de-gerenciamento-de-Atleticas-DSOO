from entidade.pessoa import Pessoa
from entidade.atletica import Atletica
from datetime import date


class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: int, data_nascimento: date, gols: int, atletica: str):
        super().__init__(nome, cpf, data_nascimento)
        self.__gols = 0
        self.__atletica = None
        if isinstance(gols, int):
            self.__gols = gols
        if isinstance(atletica, str):
            self.__atletica = atletica

    @property
    def nome(self):
        return self._Pessoa__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self._Pessoa__nome = nome

    @property
    def cpf(self):
        return self._Pessoa__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self._Pessoa__cpf = cpf

    @property
    def data_nascimento(self):
        return self._Pessoa__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        if isinstance(data_nascimento, date):
            self._Pessoa__data_nascimento = data_nascimento

    @property
    def atletica(self):
        return self.__atletica

    @property
    def gols(self):
        return self.__gols

    @gols.setter
    def gols(self, gols: int):
        if isinstance(gols, int):
            self.__gols = gols

    def incrementa_gol(self):
        self.__gols = self.__gols + 1
