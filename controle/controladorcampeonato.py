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
        dados_campeonato = self.__tela_campeonato.pega_dados_livro()
        l = self.pega_livro_por_codigo(dados_livro["codigo"])
        if l is None:
            livro = Livro(dados_livro["titulo"], dados_livro["codigo"])
            self.__livros.append(livro)
        else:
            self.__tela_livro.mostra_mensagem("ATENCAO: Livro já existente")

    def excluir_campeonato(self):
        pass

    def incluir_partida(self):
        pass

    def excluir_partida(self):
        pass

    def listar_partida(self):
        pass

    def classificacao(self, pontuacao):
        classificacao = dict(sorted(pontuacao.items(), key=lambda item: item[1]))
        podio = list(classificacao.keys())[:3]
        return podio

    def retornar(self):
        pass

    def tela_opcoes(self):
        pass
