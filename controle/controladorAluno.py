from entidade.aluno import Aluno
from limite.telaAluno import TelaAluno


class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()
        self.__lista_alunos = []

    def pega_aluno_por_cpf(self):
        cpf = self.__tela_aluno.pegar_dados_por_cpf()
        for aluno in self.__lista_alunos:
            if (aluno is not None) and aluno.cpf == cpf:
                return aluno
        else:
            self.__tela_aluno.mostrar_mensagem("Aluno não encontrado")

    def adiciona_aluno(self):
        dados_aluno = self.__tela_aluno.pegar_dados_aluno()
        novo_aluno = Aluno(
            dados_aluno["nome"],
            dados_aluno["cpf"],
            dados_aluno["data_nascimento"],
            dados_aluno["gols"])
        self.__lista_alunos.append(novo_aluno)

    def exclui_aluno(self):
        cpf = self.__tela_aluno.pegar_dados_por_cpf()
        for aluno in self.__lista_alunos:
            if aluno.cpf == cpf:
                print("Aluno excluido")
                return self.__lista_alunos.remove(aluno)
        self.__tela_aluno.mostrar_mensagem("Usuário não encontrado")

    def alterar_aluno(self):
        aluno = self.pega_aluno_por_cpf()

        if aluno is not None:
            novos_dados = self.__tela_aluno.pegar_dados_aluno()
            aluno.nome = novos_dados["nome"]
            aluno.cpf = novos_dados["cpf"]
            aluno.data_nascimento = novos_dados["data_nascimento"]
            aluno.gols = novos_dados["gols"]
        else:
            self.__tela_aluno.mostrar_mensagem("Aluno não existente")

    def listar_aluno(self):
        for aluno in self.__lista_alunos:
            self.__tela_aluno.mostrar_dados_aluno({
                "nome": aluno.nome,
                "cpf": aluno.cpf,
                "data_nascimento": aluno.data_nascimento,
                "gols": aluno.gols})

    def inicializa_sistema(self):
        self.abre_tela()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_aluno, 2: self.exclui_aluno,
                        3: self.alterar_aluno, 4: self.listar_aluno,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
