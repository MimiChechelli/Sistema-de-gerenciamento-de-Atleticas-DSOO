from entidade.arbitro import Arbitro
from limite.telaArbitro import TelaArbitro


class ControladorAluno():
    def __init__(self):
        self.__tela_arbitro = TelaArbitro()
        self.__lista_arbitros = []

    def pega_arbitro_por_cpf(self, cpf: int):
        if isinstance(cpf, int):
            for arbitro in self.__lista_arbitros:
                if arbitro.cpf == cpf:
                    return arbitro
        else:
            self.__tela_arbitro.mostrar_mensagem("Aluno não encontrado")

    def adiciona_arbitro(self):
        dados_arbitro = self.__tela_arbitro.pegar_dados_arbitro()
        novo_arbitro = Arbitro(
            dados_arbitro["nome"],
            dados_arbitro["cpf"],
            dados_arbitro["data_nascimento"],
            dados_arbitro["numero_partidas"])
        self.__lista_arbitros.append(novo_arbitro)

    def exclui_arbitro(self, cpf):
        for arbitro in self.__lista_arbitros:
            if arbitro.cpf == cpf:
                self.__lista_arbitros.remove(arbitro)
        self.__tela_arbitro.mostrar_mensagem("Usuário não encontrado")

    def alterar_arbitro(self):
        cpf = self.__tela_arbitro.pegar_dados_por_cpf()
        arbitro = self.pega_arbitro_por_cpf(cpf)

        if arbitro is not None:
            novos_dados = self.__tela_amigo.pegar_dados_arbitro()
            arbitro.nome = novos_dados["nome"]
            arbitro.cpf = novos_dados["cpf"]
            arbitro.data_nascimento = novos_dados["data_nascimento"]
            arbitro.numero_partidas = novos_dados["numero_partidas"]
        else:
            self.__tela_arbitro.mostrar_mensagem("Arbitro não existente")

    def listar_arbitros(self):
        for arbitro in self.__lista_arbitros:
            self.__tela_arbitro.mostrar_dados_arbitro({
                "nome": arbitro.nome,
                "cpf": arbitro.cpf,
                "data_nascimento": arbitro.data_nascimento,
                "numero_partidas": arbitro.numero_partidas})

    def inicializa_sistema(self):
        self.abre_tela()

    def retornar(self):
        exit()

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_arbitro, 2: self.exclui_arbitro,
                        3: self.alterar_arbitro, 4: self.listar_arbitros,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_arbitro.tela_opcoes()]()