from limite.telaSistema import TelaSistema
from controle.controladorAluno import ControladorAluno
from controle.controladorArbitro import ControladorArbitro
from controle.controladorAtletica import ControladorAtletica
from controle.controladorPartida import ControladorPartida
from controle.controladorCampeonato import ControladorCampeonato


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_arbitro = ControladorArbitro(self)
        self.__controlador_atletica = ControladorAtletica(self)
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_campeonato = ControladorCampeonato(self)

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    @property
    def controlador_arbitro(self):
        return self.__controlador_arbitro

    @property
    def controlador_atletica(self):
        return self.__controlador_atletica

    @property
    def controlador_partida(self):
        return self.__controlador_partida

    @property
    def controlador_campeonato(self):
        return self.__controlador_campeonato

    def cadastra_aluno(self):
        self.__controlador_aluno.abre_tela()

    def cadastra_arbitro(self):
        self.__controlador_arbitro.abre_tela()

    def cadastra_atletica(self):
        self.__controlador_atletica.abre_tela()

    def cadastra_partida(self):
        self.__controlador_partida.abre_tela()

    def cadastra_campeonato(self):
        self.__controlador_campeonato.abre_tela()

    def encerra_sistema(self):
        exit()

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_aluno, 2: self.cadastra_arbitro,
                        3: self.cadastra_atletica, 4: self.cadastra_partida, 5: self.cadastra_campeonato}

        while True:
            lista_opcoes[self.__tela_sistema.tela_opcoes()]()
