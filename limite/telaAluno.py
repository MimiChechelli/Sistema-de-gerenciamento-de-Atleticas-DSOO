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
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- DADOS DO ALUNO ----------', font=("Helvica", 25))],
        [sg.Text('Nome do aluno:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('CPF do aluno:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Text('Insira a data de nascimento:', size=(15, 1)), sg.InputText('AAAA-MM-DD', key='data_nascimento')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        cpf = values['cpf']
        nome = values['nome']
        data_nascimento = values['data_nascimento']
        self.close()
        return {"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento}

    # def mostrar_dados_aluno(self, dados_aluno):
    #     print("Nome: ", dados_aluno["nome"])
    #     print("Cpf ", dados_aluno["cpf"])
    #     print("Data de nascimento ", dados_aluno["data_nascimento"])
    #     print("Gols", dados_aluno["gols"])
    #     print("\n")

    # def pegar_dados_por_cpf(self):
    #     cpf = int(input("Digite o CPF do aluno que deseja selecionar: "))
    #     return cpf

    def mostrar_alunos(self,lista_alunos):
        cursos = sorted(set(aluno.cpf for aluno in lista_alunos))
        layout_curso = [
            [sg.Text('Selecione o CPF do aluno')],
            [sg.Listbox(values=cursos, size=(30, 6), key='aluno_selecionado')],
            [sg.Button('Selecionar aluno')]
        ]
        window = sg.Window('Seleção de Aluno').Layout(layout_curso)
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED:
            window.close()
            return None
        aluno_selecionado = valores['aluno_selecionado'][0] if valores['aluno_selecionado'] else None
        window.close()
        if not aluno_selecionado:
            return None
        return aluno_selecionado

    def mostra_mensagem(self, msg):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [[sg.Text(f'{msg}', font=("Helvica", 25))]]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        self.close()
