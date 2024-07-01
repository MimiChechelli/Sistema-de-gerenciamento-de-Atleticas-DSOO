from entidade.arbitro import Arbitro
from limite.telaArbitro import TelaArbitro
from dao.arbitroDao import ArbitroDAO


class ControladorArbitro():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_arbitro = TelaArbitro()
        self.__arbitro_dao = ArbitroDAO()

    def pega_arbitro_por_cpf(self):
        cpf = self.__tela_arbitro.pegar_dados_arbitro()
        arbitro = self.__arbitro_dao.get(cpf)
        if arbitro:
            return arbitro
        else:
            self.__tela_arbitro.mostrar_mensagem(
                "Arbitro não encontrado")  # Alterar tela

    def adiciona_arbitro(self):
        dados_arbitro = self.__tela_arbitro.pegar_dados_arbitro()
        novo_arbitro = Arbitro(
            dados_arbitro["nome"],
            dados_arbitro["cpf"],
            dados_arbitro["data_nascimento"],
            dados_arbitro["numero_partidas"])
        self.__arbitro_dao.add(novo_arbitro)  # Alterar tela

    def exclui_arbitro(self):
        cpf = self.__tela_arbitro.pegar_dados_por_cpf()
        if self.__arbitro_dao.remove(cpf):
            self.__tela_arbitro.mostra_mensagem(
                "Arbitro excluído")  # Alterar tela
        else:
            self.__tela_arbitro.mostrar_mensagem(
                "Arbitro não encontrado")  # Alterar tela

    def alterar_arbitro(self):
        arbitro = self.pega_arbitro_por_cpf()
        if arbitro is not None:
            novos_dados = self.__tela_arbitro.pegar_dados_arbitro()
            arbitro.nome = novos_dados["nome"]
            arbitro.cpf = novos_dados["cpf"]
            arbitro.data_nascimento = novos_dados["data_nascimento"]
            arbitro.numero_partidas = novos_dados["numero_partidas"]
            self.__arbitro_dao.add(arbitro)
        else:
            self.__tela_arbitro.mostrar_mensagem("Arbitro não existente")

    def listar_arbitros(self):
        lista_arbitros = self.__aluno_dao.get_all()
        for arbitro in lista_arbitros:
            self.__tela_arbitro.mostrar_dados_arbitro({
                "nome": arbitro.nome,
                "cpf": arbitro.cpf,
                "data_nascimento": arbitro.data_nascimento,
                "numero_partidas": arbitro.numero_partidas})

    def inicializa_sistema(self):
        self.abre_tela()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):  # Alterar tela
        lista_opcoes = {1: self.adiciona_arbitro, 2: self.exclui_arbitro,
                        3: self.alterar_arbitro, 4: self.listar_arbitros,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_arbitro.tela_opcoes()]()
