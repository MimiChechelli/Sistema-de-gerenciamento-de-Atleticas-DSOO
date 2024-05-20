from entidade.atletica import Atletica
from limite.telaatletica import TelaAtletica

class ControladorAtletica():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_atletica = TelaAtletica(self)
        self.__atleticas = []


    def lista_atletica(self):
        for a in self.__atleticas:
            self.__tela_atletica.mostrar_dados_atletica({"nome": a.nome,
                                                        "curso": a.curso,
                                                        "alunos": a.alunos})

    def pega_atletica_pelo_curso(self, curso):
        for atletica in self.__atleticas:
            if(atletica.curso == curso):
                return atletica
        return None

    def pega_atletica_pelo_nome(self, nome):
        for atletica in self.__atleticas:
            if(atletica.nome == nome):
                return atletica
        return None

    def incluir_atletica(self):
        dados_atletica = self.__tela_atletica.pegar_dados_atletica()
        a = self.pega_atletica_pelo_curso(dados_atletica["curso"])
        if a is None:
            atletica = Atletica(dados_atletica["curso"], dados_atletica["nome"])
            self.__atleticas.append(atletica)
        else:
            self.__tela_atletica.mostra_mensagem("ATENCAO: Atletica já existente")

    def excluir_atletica(self):
        self.lista_atletica()
        curso_atletica = self.__tela_livro.seleciona_atletica()
        atletica = self.pega_atletica_pelo_curso(curso_atletica)
        if(atletica is not None):
            self.__atleticas.remove(atletica)
            self.lista_atletica()
        else:
            self.__tela_atletica.mostra_mensagem("ATENCAO: Atletica não existente")

    def incluir_aluno_em_atletica(self):
        self.__tela_atletica.mostra_mensagem("Na atlética de qual curso deseja incluir? ")
        self.lista_atletica()
        curso_atletica = self.__tela_atletica.seleciona_atletica()
        atletica = self.pega_atletica_pelo_curso(curso_atletica)
        if(atletica is not None):
            aluno = None # ver com o Gab
            atletica.adc_aluno(aluno)
        else:
            self.__tela_atletica.mostra_mensagem("ATENCAO: Atletica não existente")

    def excluir_aluno_de_atletica(self):
        self.__tela_atletica.mostra_mensagem("Na atlética de qual curso deseja excluir? ")
        self.lista_atletica()
        curso_atletica = self.__tela_livro.seleciona_atletica()
        atletica = self.pega_atletica_pelo_curso(curso_atletica)
        if(atletica is not None):
            aluno = None # ver com o Gab
            atletica.remove_aluno(aluno)
        else:
            self.__tela_atletica.mostra_mensagem("ATENCAO: Atletica não existente")

    def listar_aluno(self):
        self.__tela_atletica.mostra_mensagem("Deseja listar de qual atlética? ")
        self.lista_atletica()
        curso_atletica = self.__tela_atletica.seleciona_atletica()
        atletica = self.pega_atletica_pelo_curso(curso_atletica)
        if(atletica is not None):
            for aluno in atletica.__alunos:
                mostrar_dados_aluno(aluno) # Gab
        else:
            self.__tela_atletica.mostra_mensagem("ATENCAO: Atletica não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_atletica, 2: self.excluir_atletica, 
                        3: self.incluir_aluno_em_atletica, 4: self.excluir_aluno_de_atletica,
                        5: self.listar_aluno, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_atletica.tela_opcoes()]()
