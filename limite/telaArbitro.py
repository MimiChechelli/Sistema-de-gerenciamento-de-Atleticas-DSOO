from datetime import date, datetime
import PySimpleGUI as sg

class TelaArbitro():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- ARBITRO ----------', font=("Helvica", 25))],
            [sg.Button('Cadastrar arbitro',key='1')],
            [sg.Button('Excluir arbitro',key='2')],
            [sg.Button('Alterar arbitro',key='3')],
            [sg.Button('Listar arbitro', key='4')],
            [sg.Button('Retornar', key='0')]
        ]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        self.close()
        return int(button)

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
