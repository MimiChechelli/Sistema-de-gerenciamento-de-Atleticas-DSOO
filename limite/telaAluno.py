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
        print("\n")
        return opcao

    def pegar_dados_aluno(self):
        print("*** DADOS DO ALUNO ***")
        nome = input("Nome: ")
        cpf = int(input("CPF (somente números): "))
        data_nascimento = input("Insira a data de nascimento: (AAAA-MM-DD) ")
        data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        gols = int(input("Quantidade de Gols: "))
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(gols, int) and isinstance(data_nascimento, date):
            return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "gols": gols}
            print("\n")
        print("Algum dos dados foi inserido de forma errada, favor repetir")
        print("\n")

    def mostrar_dados_aluno(self, dados_aluno):
        print("Nome: ", dados_aluno["nome"])
        print("Cpf ", dados_aluno["cpf"])
        print("Data de nascimento ", dados_aluno["data_nascimento"])
        print("Gols", dados_aluno["gols"])
        print("\n")

    def pegar_dados_por_cpf(self):
        cpf = int(input("Digite o CPF do aluno que deseja selecionar: "))
        return cpf

    def mostrar_mensagem(self, mensagem: str):
        print(mensagem)
