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
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- DADOS DO ARBITRO ----------', font=("Helvica", 25))],
        [sg.Text('Nome do arbitro:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('CPF do arbitro:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Text('Insira a data de nascimento:', size=(15, 1)), sg.InputText('AAAA-MM-DD', key='data_nascimento')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        cpf = values['cpf']
        nome = values['nome']
        data_nascimento = values['data_nascimento']
        self.close()
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(data_nascimento, date):
            return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "numero_partidas": 0}
        print("Algum dos dados foi inserido de forma errada, favor repetir")
        print("\n")

    # Códigos anteriores:
    # def mostrar_dados_arbitro(self, dados_arbitro):
    #     print("Nome: ", dados_arbitro["nome"])
    #     print("Cpf: ", dados_arbitro["cpf"])
    #     print("Data nascimento: ", dados_arbitro["data_nascimento"])
    #     print("Numero partidas: ", dados_arbitro["numero_partidas"])
    #     print("\n")

    # def pegar_dados_por_cpf(self):
    #     cpf = int(input("Digite o CPF do arbitro que deseja selecionar: "))
    #     if isinstance(cpf, int):
    #         return cpf
    #     else:
    #         print("Não foi possível encontrar esse CPF")
    #         print("\n")

    def mostrar_arbitro(self, lista_arbitros):
        cpf = sorted(set(arbitro.cpf for arbitro in lista_arbitros))
        layout = [
            [sg.Text('Selecione o CPF do arbitro')],
            [sg.Listbox(values=cpf, size=(30, 6), key='arbitro_selecionado')],
            [sg.Button('Selecionar arbitro')]
        ]
        window = sg.Window('Seleção de arbitro').Layout(layout)
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED:
            window.close()
            return None
        arbitro_selecionado = valores['arbitro_selecionado'][0] if valores['arbitro_selecionado'] else None
        window.close()
        if not arbitro_selecionado:
            return None
        return arbitro_selecionado

    def mostra_mensagem(self, msg):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [[sg.Text(f'{msg}', font=("Helvica", 25))]]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        self.close()
