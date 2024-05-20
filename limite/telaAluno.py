from datetime import datetime, date
from entidade.atletica import Atletica


class TelaAluno():
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("--- ESCOLHA A OPÇÃO DESEJADA ---")
        print("1 - Cadastrar aluno")
        print("2 - Excluir aluno")
        print("3 - Alterar aluno")
        print("4 - Listar alunos")
        print("0 - Retornar ao menu")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pegar_dados_aluno(self):
        print("*** DADOS DO ALUNO ***")
        nome = input("Nome: ")
        cpf = int(input("CPF (somente números): "))
        data_nascimento = input("Insira a data de nascimento: (AAAA-MM-DD) ")
        data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        gols = int(input("Quantidade de Gols: "))
        atletica = input("Nome da atletica (não é permitido alterar): ")

# descobrir um jeito de verificar a atletica

        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(gols, int) and isinstance(atletica, str) and isinstance(data_nascimento, date):
            return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "gols": gols, "atletica": atletica}
        print("Algum dos dados foi inserido de forma errada, favor repetir")

    def mostrar_dados_aluno(self, dados_aluno):
        print("Nome: ", dados_aluno["nome"])
        print("Cpf ", dados_aluno["cpf"])
        print("Data de nascimento ", dados_aluno["data_nascimento"])
        print("Gols", dados_aluno["gols"])
        print("Atletica", dados_aluno["atletica"])
        print("\n")

    def pegar_dados_por_cpf(self):
        cpf = input("Digite o CPF do aluno que deseja selecionar: ")
        cpf = int(cpf)
        if isinstance(cpf, int):
            return cpf
        else:
            print("Não foi possível encontrar esse CPF")

    def mostrar_mensagem(self, mensagem: str):
        print(mensagem)
