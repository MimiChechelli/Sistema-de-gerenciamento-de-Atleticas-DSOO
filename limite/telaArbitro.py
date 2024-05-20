from datetime import date, datetime


class TelaArbitro():
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("--- ESCOLHA A OPÇÃO DESEJADA ---")
        print("1 - Cadastrar arbitro")
        print("2 - Excluir arbitro")
        print("3 - Alterar arbitro")
        print("4 - Listar arbitros")
        print("0 - Retornar ao menu")
        opcao = int(input("Escolha a opcao: "))
        print("\n")
        return opcao

    def pegar_dados_arbitro(self):
        print("*** DADOS DO ARBITRO ***")
        nome = input("Nome: ")
        cpf = int(input("CPF (somente números): "))
        data_nascimento = input("Data de nascimento (YYYY,MM,DD): ")
        data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        numero_partidas = int(input("Quantidade de partidas: "))
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(numero_partidas, int) and isinstance(data_nascimento, date):
            print("\n")
            return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "numero_partidas": numero_partidas}
        print("Algum dos dados foi inserido de forma errada, favor repetir")
        print("\n")

    def mostrar_dados_arbitro(self, dados_arbitro):
        print("Nome: ", dados_arbitro["nome"])
        print("Cpf: ", dados_arbitro["cpf"])
        print("Data nascimento: ", dados_arbitro["data_nascimento"])
        print("Numero partidas: ", dados_arbitro["numero_partidas"])
        print("\n")

    def pegar_dados_por_cpf(self):
        cpf = int(input("Digite o CPF do arbitro que deseja selecionar: "))
        if isinstance(cpf, int):
            return cpf
        else:
            print("Não foi possível encontrar esse CPF")
            print("\n")

    def mostrar_mensagem(self, mensagem: str):
        print(mensagem)
