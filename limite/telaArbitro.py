from datetime import date


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
        return opcao

    def pegar_dados_arbitro(self):
        print("*** DADOS DO ARBITRO ***")
        nome = input("Nome: ")
        cpf = int(input("CPF (somente números): "))
        data_nascimento = date(input("Data de nascimento (YYYY,MM,DD): "))
        numero_partidas = input("Quantidade de partidas: ")
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(numero_partidas, int) and isinstance(data_nascimento, date):
            return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "numero_partidas": numero_partidas}
        print("Algum dos dados foi inserido de forma errada, favor repetir")

    def mostrar_dados_arbitro(self, dados_arbitro):
        print("Nome: ", dados_arbitro["nome"])
        print("Cpf: ", dados_arbitro["cpf"])
        print("Data nascimento: ", dados_arbitro["data_nascimento"])
        print("Numero partidas: ", dados_arbitro["numero_partidas"])
        print("\n")

    def pegar_dados_por_cpf(self):
        cpf = input("Digite o CPF do arbitro que deseja selecionar: ")
        if isinstance(cpf, int):
            return cpf
        else:
            print("Não foi possível encontrar esse CPF")

    def mostrar_mensagem(self, mensagem: str):
        print(mensagem)
