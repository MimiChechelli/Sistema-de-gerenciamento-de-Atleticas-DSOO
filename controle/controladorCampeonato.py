from entidade.campeonato import Campeonato
from limite.telaCampeonato import TelaCampeonato
from dao.campeonatoDao import CampeonatoDAO


class ControladorCampeonato():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_campeonato = TelaCampeonato(self)
        self.__campeonato_dao = CampeonatoDAO()

    def campeonatos(self):
        return self.__campeonato_dao.get_all()

    def pega_campeonato_pela_edicao(self, edicao: int):
        return self.__campeonato_dao.get(edicao)

    def incluir_campeonato(self):
        edicao = self.__tela_campeonato.pegar_dados_campeonato()
        c = self.pega_campeonato_pela_edicao(edicao)
        if c is None:
            campeonato = Campeonato(edicao)
            self.__campeonatos_dao.add(campeonato)
            self.__tela_campeonato.mostra_mensagem(
                f"Campeonato {edicao} cadastrado\n")
        else:
            self.__tela_campeonato.mostra_mensagem(
                "ATENCAO: Campeonato já existente\n")

    def excluir_campeonato(self):
        edicao = self.__tela_campeonato.pega_edicao()
        if self.__campeonato_dao.remove(edicao):
            self.__tela_campeonato.mostra_mensagem("Campeonato deletado\n")
        else:
            self.__tela_campeonato.mostra_mensagem(
                "ATENCAO: Campeonato não existente\n")

    def incluir_partida(self):
        self.__tela_campeonato.lista_edicoes(self.__campeonatos)
        dados_campeonato = self.__tela_campeonato.pega_edicao()
        c = self.pega_campeonato_pela_edicao(dados_campeonato)
        if c is not None:
            self.__controlador_sistema.controlador_partida.listar_partida()
            codigo = int(
                # Alterar tela
                input("insira o codigo da partida que deseja adicionar: "))
            for partida in c.partidas:
                if partida.codigo == codigo:
                    return self.__tela_campeonato.mostra_mensagem("ATENCAO: Partida já registrada\n")
            for partida in self.__controlador_sistema.controlador_partida.partidas:
                if partida.codigo == codigo:
                    c.partidas.append(partida)
                    if partida.atletica_1 in c.pontuacao:
                        c.pontuacao[partida.atletica_1] = c.pontuacao.get(
                            partida.atletica_1, 0) + partida.resultado_atl_1
                    else:
                        c.pontuacao[partida.atletica_1] = partida.resultado_atl_1
                    if partida.atletica_2 in c.pontuacao:
                        c.pontuacao[partida.atletica_2] = c.pontuacao.get(
                            partida.atletica_2, 0) + partida.resultado_atl_2
                    else:
                        c.pontuacao[partida.atletica_2] = partida.resultado_atl_2
                    self.__campeonato_dao.add(c)  # Atualiza dao
                    return self.__tela_campeonato.mostra_mensagem("Partida registrada!\n")
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Campeonato não existente"
                                                   "\n")

    def excluir_partida(self):
        self.__tela_campeonato.lista_edicoes(self.__campeonatos)
        edicao = self.__tela_campeonato.pega_edicao()
        c = self.pega_campeonato_pela_edicao(edicao)
        if c is not None:
            for partida in c.partidas:
                self.__controlador_sistema.controlador_partida.mostra_partida(
                    partida)
            codigo = self.__controlador_sistema.controlador_partida.tela_partida.pegar_codigo_partida()
            for partida in c.partidas:
                if partida.codigo == codigo:
                    c.partidas.remove(partida)
                    self.__campeonato_dao.add(c)  # Atualiza o campeonato DAO
                    self.__tela_campeonato.mostra_mensagem("Partida excluida")
                    return
                self.__tela_campeonato.mostra_mensagem(
                    "ATENCAO: Partida não encontrada\n")
        else:
            self.__tela_campeonato.mostra_mensagem(
                "ATENCAO: Campeonato não existente")

    def listar_partida(self):
        self.__tela_campeonato.lista_edicoes(self.__campeonatos)
        edicao = self.__tela_campeonato.pega_edicao()
        c = self.pega_campeonato_pela_edicao(edicao)
        if c is not None:
            for partida in c.partidas:
                self.__controlador_sistema.controlador_partida.mostra_partida(
                    partida)
        else:
            self.__tela_campeonato.mostra_mensagem(
                "ATENCAO: Campeonato não existente")

    def classificacao(self):
        self.__tela_campeonato.lista_edicoes(self.__campeonatos)
        edicao = self.__tela_campeonato.pega_edicao()
        c = self.pega_campeonato_pela_edicao(edicao)
        if c is not None:
            pontuacao = c.pontuacao
            classificacao = dict(
                sorted(pontuacao.items(), key=lambda item: item[1]))
            podio = list(classificacao.keys())[:3]
            self.__tela_campeonato.mostrar_ranking_campeonato(podio)
        else:
            self.__tela_campeonato.mostra_mensagem(
                "Campeonato não existente\n")  # Alterar tela

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_campeonato, 2: self.excluir_campeonato,
                        3: self.incluir_partida, 4: self.excluir_partida,
                        5: self.listar_partida, 6: self.classificacao, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_campeonato.tela_opcoes()]()
