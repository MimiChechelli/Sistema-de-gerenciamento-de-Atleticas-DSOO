from datetime import datetime, date
from entidade.atletica import Atletica
import PySimpleGUI as sg

class TelaAluno():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- ALUNOS ----------', font=("Helvica", 25))],
            [sg.Button('Cadastrar alunos',key='1')],
            [sg.Button('Excluir aluno',key='2')],
            [sg.Button('Alterar aluno',key='3')],
            [sg.Button('Listar alunos', key='4')],
            [sg.Button('Retornar', key='0')]
        ]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        self.close()
        return int(button)

    def pegar_dados_aluno(self):
        print("*** DADOS DO ALUNO ***")
        nome = input("Nome: ")
        cpf = int(input("CPF (somente números): "))
        data_nascimento = input("Insira a data de nascimento: (AAAA-MM-DD) ")
        data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        gols = int(input("Quantidade de Gols: "))
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(gols, int) and isinstance(data_nascimento, date):
            print("\n")
            return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "gols": gols}
        print("Algum dos dados foi inserido de forma errada")
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
