from entidade.partida import Partida

class Campeonato():
    def __init__(self, edicao):
        self.__edicao = edicao
        self.__pontuacao = {}
        self.__partidas = []


    @property
    def edicao(self):
        return self.__edicao

    @property
    def pontuacao(self):
        return self.__pontuacao

    @property
    def partidas(self):
        return self.__partidas
