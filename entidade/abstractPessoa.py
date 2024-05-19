from abc import ABC, abstractmethod
from datetime import date


class AbstractPessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, cpf: int, data_nascimento: date):
        self.__nome = None
        self.__cpf = None
        self.__data_nascimento = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(data_nascimento, date):
            self.__data_nascimento = data_nascimento

    @property
    @abstractmethod
    def nome(self):
        return self.__nome

    @nome.setter
    @abstractmethod
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    @abstractmethod
    def cpf(self):
        return self.__cpf

    @cpf.setter
    @abstractmethod
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self.__cpf = cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        if isinstance(data_nascimento, date):
            self.__data_nascimento = data_nascimento
