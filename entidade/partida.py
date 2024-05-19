from entidade.atletica import Atletica
from entidade.arbitro import Arbitro

class Partida():
    def __init__(self, codigo,  data_partida, atletica_1, atletica_2, arbitro, resultado_atl_1, resultado_atl_2):
        self.__codigo = codigo
        self.__data_partida = data_partida
        if(isinstance(atletica_1, Atletica)):
            self.__atletica_1 = atletica_1
        if(isinstance(atletica_2, Atletica)):
            self.__atletica_2 = atletica_2
        if(isinstance(arbitro, Arbitro)):
            self.__arbitro = arbitro
        self.__resultado_atl_1 = resultado_atl_1
        self.__resultado_atl_2 = resultado_atl_2

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo

    @property
    def data_partida(self):
        return self.__data_partida

    @data_partida.setter
    def data_partida(self, data_partida):
        self.__data_partida = data_partida

    @property
    def atletica_1(self):
        return self.__atletica_1

    @atletica_1.setter
    def atletica_1(self, atletica):
        self.__atletica_1 = atletica

    @property
    def atletica_2(self):
        return self.__atletica_2

    @atletica_2.setter
    def atletica_2(self, atletica):
        self.__atletica_2 = atletica

    @property
    def arbitro(self):
        return self.__arbitro

    @arbitro.setter
    def arbitro(self, arbitro):
        self.__arbitro = arbitro

    @property
    def resultado_atl_1(self):
        return self.__resultado_atl_1

    @resultado_atl_1.setter
    def resultado_atl_1(self, resultado_atl_1):
        self.__resultado_atl_1 = resultado_atl_1

    @property
    def resultado_atl_2(self):
        return self.__resultado_atl_2

    @resultado_atl_2.setter
    def resultado_atl_2(self, resultado_atl_2):
        self.__resultado_atl_2 = resultado_atl_2

    def vencedor(self):
        if(self.__resultado_atl_2 == self.__resultado_atl_1):
            return None
        elif(self.__resultado_atl_2 > self.__resultado_atl_1):
            return self.__resultado_atl_2
        else:
            self.__resultado_atl_1
