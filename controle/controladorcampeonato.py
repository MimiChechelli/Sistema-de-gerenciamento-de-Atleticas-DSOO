from entidade.campeonato import Campeonato
from limite.telacampeonato import TelaCampeonato
from controle.controladorPartida import ControladorPartida

class ControladorCampeonato():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_campeonato = TelaCampeonato()
        self.__campeonatos = []
        self.__controlador_partida = ControladorPartida(self)


    def pega_campeonato_pela_edicao(self, edicao: int):
        for campeonato in self.__campeonatos:
            if(campeonato.edicao == edicao):
                return campeonato
        return None

    def incluir_campeonato(self):
        dados_campeonato = self.__tela_campeonato.pegar_dados_campeonato()
        c = self.pega_campeonato_pela_edicao(dados_campeonato["edicao"])
        if c != None:
            campeonato = Campeonato(dados_campeonato["edicao"])
            self.__campeonatos.append(campeonato)
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Campeonato já existente")

    def excluir_campeonato(self):
        dados_campeonato = self.__tela_campeonato.pegar_dados_campeonato()
        c = self.pega_campeonato_pela_edicao(dados_campeonato["edicao"])
        if c != None:
            campeonato = Campeonato(dados_campeonato["edicao"])
            self.__campeonatos.remove(campeonato)
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Campeonato não existente")

    def incluir_partida(self):
        dados_campeonato = self.__tela_campeonato.pegar_dados_campeonato()
        c = self.pega_campeonato_pela_edicao(dados_campeonato["edicao"])
        if c != None:
            self.__controlador_partida.listar_partida
            codigo = input("insira o codigo da partida que deseja adicionar: ")
            for partida in c.partidas:
                if partida.codigo == codigo:
                    return self.__tela_campeonato.mostra_mensagem("ATENCAO: Partida já registrada")
            c.partidas.append(partida)
            self.__tela_campeonato.mostra_mensagem("Partida registrada!")
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Campeonato não existente")

    def excluir_partida(self):
        dados_campeonato = self.__tela_campeonato.pegar_dados_campeonato()
        c = self.pega_campeonato_pela_edicao(dados_campeonato["edicao"])
        if c != None:
            for partida in c.partidas:
                self.__tela_campeonato.mostrar_dados_campeonato
            codigo = input(" Insira o código da partida que deseja excluir: ")
            for partida in c.partidas:
                if partida.codigo == codigo:
                    c.partidas.remove(partida)
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Campeonato não existente") 

    def listar_partida(self):
        dados_campeonato = self.__tela_campeonato.pegar_dados_campeonato()
        c = self.pega_campeonato_pela_edicao(dados_campeonato["edicao"])
        if c != None:
            self.__controlador_partida.listar_partida
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Campeonato não existente") 

    def classificacao(self, pontuacao):
        classificacao = dict(sorted(pontuacao.items(), key=lambda item: item[1]))
        podio = list(classificacao.keys())[:3]
        return podio

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def tela_opcoes(self):
        lista_opcoes = {1: self.incluir_campeonato, 2: self.excluir_campeonato, 
                        3: self.incluir_partida, 4: self.excluir_partida,
                        5: self.listar_partida, 6: self.classificacao, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_campeonato.tela_opcoes()]()
            

