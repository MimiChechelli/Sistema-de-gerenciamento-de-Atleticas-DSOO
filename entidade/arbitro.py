from entidade.pessoa import Pessoa
from datetime import date


class Arbitro(Pessoa):
    def __init__(self, nome: str, cpf: int, data_nascimento: date, numero_partidas: int):
        super().__init__(nome, cpf, data_nascimento)
        self.__numero_partidas = None
        if isinstance(numero_partidas, int):
            self.__numero_partidas = numero_partidas

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
    def numero_partidas(self):
        return self.__numero_partidas

    @numero_partidas.setter
    def numero_partidas(self, numero_partidas: int):
        if isinstance(numero_partidas, int):
            self.__numero_partidas = numero_partidas

    def incrementa_partidas(self):
        self.__numero_partidas = self.__numero_partidas + 1
