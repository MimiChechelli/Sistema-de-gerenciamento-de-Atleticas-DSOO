from entidade.partida import Partida
from limite.telaPartida import TelaPartida
from entidade.atletica import Atletica
from entidade.arbitro import Arbitro

class ControladorPartida():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_partida = TelaPartida()
        self.__partidas = []

    @property
    def tela_partida(self):
        return self.__tela_partida

    @property
    def partidas(self):
        return self.__partidas

    def pega_partida_pelos_dados(self, codigo):
        for partida in self.__partidas:
            if codigo == partida.codigo:
                return partida
        return None

    def incluir_partida(self):
        codigo, data_partida, atletica_1, atletica_2, arbitro, resultado_atl_1, resultado_atl_2 = self.__tela_partida.pegar_dados_partida()
        p = self.pega_partida_pelos_dados(codigo)
        if p is None:
            partida = Partida(codigo, data_partida, atletica_1, atletica_2, arbitro, resultado_atl_1, resultado_atl_2)
            self.__partidas.append(partida)
            self.__tela_partida.mostra_mensagem("Partida cadastrada"
                                                "\n")
        else:
            self.__tela_partida.mostra_mensagem("ATENCAO: Partida já existente")

    def alterar_partida(self):
        self.listar_partida
        codigo = self.__tela_partida.pegar_codigo_partida()
        for p in self.__partidas:
            if p.codigo == codigo:
                codigo_nv, data_partida_nv, atletica_1_nv, atletica_2_nv, arbitro_nv, resultado_atl_1_nv, resultado_atl_2_nv = self.__tela_partida.pegar_dados_partida()
                p.codigo = codigo_nv
                p.data_partida = data_partida_nv
                p.atletica_1 = atletica_1_nv
                p.atletica_2 = atletica_2_nv
                p.arbitro = arbitro_nv
                p.resultado_atl_1 = resultado_atl_1_nv
                p.resultado_atl_2 = resultado_atl_2_nv
                return self.__tela_partida.mostra_mensagem("Partida alterada")
        self.__tela_partida.mostra_mensagem("Partida não encontrada")

    def excluir_partida(self):
        codigo = self.__tela_partida.pegar_codigo_partida()
        p = self.pega_partida_pelos_dados(codigo)
        if p is None:
            self.__tela_partida.mostra_mensagem("ATENCAO: Partida inexistente")
        else:
            self.__partidas.remove(p)
            self.__tela_partida.mostra_mensagem("Partida removida")

    def listar_partida(self):
        for p in self.__partidas:
            self.__tela_partida.mostrar_dados_partida({"codigo": p.codigo,
                                                        "data_partida": p.data_partida,
                                                        "atletica_1": p.atletica_1,
                                                        "atletica_2": p.atletica_2,
                                                        "arbitro": p.arbitro,
                                                        "resultado_atl_1": p.resultado_atl_1,
                                                        "resultado_atl_2": p.resultado_atl_1})

    def mostra_partida(self, partida):
        self.__tela_partida.mostrar_dados_partida({"codigo": partida.codigo,
                                                    "data_partida": partida.data_partida,
                                                    "atletica_1": partida.atletica_1,
                                                    "atletica_2": partida.atletica_2,
                                                    "arbitro": partida.arbitro,
                                                    "resultado_atl_1": partida.resultado_atl_1,
                                                    "resultado_atl_2": partida.resultado_atl_1})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_partida, 2: self.alterar_partida, 
                        3: self.excluir_partida, 4: self.listar_partida,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_partida.tela_opcoes()]()
