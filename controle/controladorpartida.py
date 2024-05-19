from entidade.partida import Partida
from limite.telapartida import TelaPartida

class ControladorPartida():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_partida = TelaPartida()
        self.__partidas = []


    def pega_partida_pelos_dados(self, dados):
        for partida in self.__partidas:
            if(partida.data_partida == dados["data_partida"]):
                if(partida.atletica_1 == dados["atletica_1"] and partida.atletica_2 == dados["atletica_2"]) or (partida.atletica_1 == dados["atletica_2"] and partida.atletica_2 == dados["atletica_1"]):
                    if(partida.arbitro == dados["arbitro"]):
                        return partida
        return None

    def incluir_partida(self):
        dados_partida = self.__tela_partida.pegar_dados_partida()
        p = self.pega_partida_pelos_dados(dados_partida)
        if p is None:
            partida = Partida(dados_partida)
            self.__partidas.append(partida)
        else:
            self.__tela_partida.mostra_mensagem("ATENCAO: Partida já existente")

    def alterar_partida(self):
        pass

    def excluir_partida(self):
        pass

    def listar_partida(self):
        for p in self.__partidas:
            self.__tela_partida.mostrar_dados_partida({["data_partida"]: p.partida.data_partida,
                                                        ["atletica_1"]: p.partida.atletica_1,
                                                        ["atletica_2"]: p.partida.atletica_2,
                                                        ["arbitro"]: p.partida.arbitro,
                                                        ["resultado_atl_1"]: p.partida.resultado_atl_1,
                                                        ["resultado_atl_2"]: p.partida.resultado_atl_1})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def tela_opcoes(self):
        lista_opcoes = {1: self.incluir_campeonato, 2: self.excluir_campeonato, 
                        3: self.incluir_partida, 4: self.excluir_partida,
                        5: self.listar_partida, 6: self.classificacao, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_campeonato.tela_opcoes()]()
