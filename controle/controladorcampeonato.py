from entidade.campeonato import Campeonato
from limite.telacampeonato import TelaCampeonato

class ControladorCampeonato():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_campeonato = TelaCampeonato()
        self.__campeonatos = []


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
            pass # chama o controlador da partida
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Campeonato não existente") 

    def excluir_partida(self):
        dados_campeonato = self.__tela_campeonato.pegar_dados_campeonato()
        c = self.pega_campeonato_pela_edicao(dados_campeonato["edicao"])
        if c != None:
            for c.partidas # escolher partida p excluir
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Campeonato não existente") 

    def listar_partida(self):
        dados_campeonato = self.__tela_campeonato.pegar_dados_campeonato()
        c = self.pega_campeonato_pela_edicao(dados_campeonato["edicao"])
        if c != None:
            pass # chama o controlador da partida
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
            

