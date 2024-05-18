


class ControladorCampeonato():
    def __init__(self) -> None:
        self.__campeonato = []


    def pega_campeonato_pela_edicao(self, codigo: int):
        for livro in self.__livros:
            if(livro.codigo == codigo):
                return livro
        return None

    def incluir_campeonato(self):
        dados_livro = self.__tela_livro.pega_dados_livro()
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
