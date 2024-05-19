from entidade.partida import Partida
from limite.telapartida import TelaPartida
from entidade.atletica import Atletica
from entidade.arbitro import Arbitro

class ControladorPartida():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_partida = TelaPartida()
        self.__partidas = []


    def pega_partida_pelos_dados(self, codigo):
        for partida in self.__partidas:
            if codigo == self.__partidas.codigo:
                return partida
        return None

    def incluir_partida(self):
        dados_partida = self.__tela_partida.pegar_dados_partida()
        p = self.pega_partida_pelos_dados(dados_partida["codigo"])
        if p is None:
            partida = Partida(dados_partida)
            self.__partidas.append(partida)
        else:
            self.__tela_partida.mostra_mensagem("ATENCAO: Partida já existente")

    def alterar_partida(self):
        self.listar_partida
        codigo = input(" Insira o código da partida que deseja alterar: ")
        for p in self.__partidas:
            if p.codigo == codigo:
                dados = self.__tela_partida.pegar_dados_partida
                p.codigo(dados["codigo"])
                p.data_partida(dados["data_partida"])
                if(isinstance(dados["atletica_1"], Atletica)):
                    p.atletica_1(dados["atletica_1"])
                if(isinstance(dados["atletica_2"], Atletica)):
                    p.atletica_2(dados["atletica_2"])
                if(isinstance(dados["arbitro"], Arbitro)):
                    p.arbitro(dados["arbitro"])
                p.resultado_atl_1(dados["resultado_atl_1"])
                p.resultado_atl_2(dados["resultado_atl_2"])

    def excluir_partida(self):
        dados_partida = self.__tela_partida.pegar_dados_partida()
        p = self.pega_partida_pelos_dados(dados_partida["codigo"])
        if p is None:
            self.__tela_partida.mostra_mensagem("ATENCAO: Partida inexistente")
        else:
            self.__partidas.remove(p)

    def listar_partida(self):
        for p in self.__partidas:
            self.__tela_partida.mostrar_dados_partida({["codigo"]: p.partida.codigo
                                                        ["data_partida"]: p.partida.data_partida,
                                                        ["atletica_1"]: p.partida.atletica_1,
                                                        ["atletica_2"]: p.partida.atletica_2,
                                                        ["arbitro"]: p.partida.arbitro,
                                                        ["resultado_atl_1"]: p.partida.resultado_atl_1,
                                                        ["resultado_atl_2"]: p.partida.resultado_atl_1})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def tela_opcoes(self):
        lista_opcoes = {1: self.incluir_partida, 2: self.alterar_partida, 
                        3: self.excluir_partida, 4: self.listar_partida,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_campeonato.tela_opcoes()]()
