


class TelaAtletica():
    def tela_opcoes(self):
        print("┏━━━━━━━━━━━━━━━━━┓")
        print(" -------- ATLÉTICA ----------")
        print(" Escolha a opcao")
        print(" 1 - Incluir Atlética")
        print(" 2 - Excluir Atlética")
        print(" 3 - Incluir aluno em Atlética")
        print(" 4 - Excluir aluno de uma Atlética")
        print(" 5 - Listar alunos de uma Atlética")
        print(" 0 - Retornar")
        opcao = int(input(" Escolha a opção: "))
        print("┗━━━━━━━━━━━━━━━━━┛")
        print("\n")
        return opcao

    def pegar_dados_atletica(self):
        print("┏━━━━━━━━━━━━━━━━━┓")
        print(" -------- DADOS ATLÉTICA ----------")
        curso = input(" Nome do curso: ")
        nome = input(" Nome da atlética: ")
        print("┗━━━━━━━━━━━━━━━━━┛")
        print("\n")
        return { "nome":{nome}, "curso": {curso}}

    def mostrar_dados_atletica(self, dados):
        print("┏━━━━━━━━━━━━━━━━━┓")
        print(" -------- DADOS ATLÉTICA ----------")
        print(" Nome da Atlética: ", dados["nome"])
        print(" Nome do Curso: ", dados["curso"])
        print(" Participantes: ", end="")
        for elemento in dados["alunos"]:
            print(elemento, end=", ")
        print("┗━━━━━━━━━━━━━━━━━┛")
        print("\n")

    def seleciona_atletica(self):
        curso = input("Nome do curso da atlética: ")
        return curso

    def mostra_mensagem(self, msg):
        print(msg)