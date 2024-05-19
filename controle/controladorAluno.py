from entidade.aluno import Aluno
from limite.telaAluno import TelaAluno


class ControladorAluno():
    def __init__(self):
        self.__tela_aluno = TelaAluno()
        self.__lista_alunos = []

    def pega_aluno_por_cpf(self, cpf: int):
        if isinstance(cpf, int):
            for aluno in self.__lista_alunos:
                if aluno.cpf == cpf:
                    return aluno
        else:
            self.__tela_aluno.mostrar_mensagem("Aluno não encontrado")

    def adiciona_aluno(self):
        dados_aluno = self.__tela_aluno.pegar_dados_aluno()
        novo_aluno = Aluno(
            dados_aluno["nome"],
            dados_aluno["cpf"],
            dados_aluno["data_nascimento"],
            dados_aluno["gols"],
            dados_aluno["atletica"])
        self.__lista_alunos.append(novo_aluno)

    def exclui_aluno(self, cpf):
        for aluno in self.__lista_alunos:
            if aluno.cpf == cpf:
                self.__lista_alunos.remove(aluno)
        self.__tela_aluno.mostrar_mensagem("Usuário não encontrado")

    def alterar_aluno(self):
        cpf = self.__tela_aluno.pegar_dados_por_cpf()
        aluno = self.pega_aluno_por_cpf(cpf)

        if aluno is not None:
            novos_dados = self.__tela_amigo.pegar_dados_aluno()
            aluno.nome = novos_dados["nome"]
            aluno.cpf = novos_dados["cpf"]
            aluno.data_nascimento = novos_dados["data_nascimento"]
            aluno.gols = novos_dados["gols"]
            aluno.atletica = novos_dados["atletica"]
        else:
            self.__tela_aluno.mostrar_mensagem("Aluno não existente")

    def listar_aluno(self):
        for aluno in self.__lista_alunos:
            self.__tela_aluno.mostrar_dados_aluno({
                "nome": aluno.nome,
                "cpf": aluno.cpf,
                "data_nascimento": aluno.data_nascimento,
                "gols": aluno.gols,
                "atletica": aluno.atletica})

    def inicializa_sistema(self):
        self.abre_tela()

    def retornar(self):
        exit()

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_aluno, 2: self.exclui_aluno,
                        3: self.alterar_aluno, 4: self.listar_aluno,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
