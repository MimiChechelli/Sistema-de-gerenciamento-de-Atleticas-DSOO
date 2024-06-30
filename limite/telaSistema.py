import PySimpleGUI as sg

class TelaSistema:
    def __init__(self) -> None:
        self.__window = None
        self.init_components()


    def init_components(self):
            layout = [
            [sg.Text('Incluir novo cliente')],
            [sg.Text('Nome:', size=(15,1)), sg.InputText('nome', key='nome')],
            [sg.Text('CPF:', size=(15,1)), sg.InputText('cpf', key='cpf')],
            [sg.Submit(), sg.Cancel()]
            ]
            window = sg.Window('Cadastro de clientes').Layout(layout)
            button, values = window.read()

    

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.read()
        self.close()
        return button

    def close(self):
        self.__window.Close()
    
    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo')],
            [sg.Text('escolha a opção:')],
            [sg.Button('Alunos', key=1)],
            [sg.Button('Arbitros', key=2)],
            [sg.Button('Atleticas', key=3)],
            [sg.Button('Partidas', key=4)],
            [sg.Button('Campeonato', key=5)],
            [sg.Button('Encerrar', key=0)],
        ]
        self.__window = sg.Window('Sistema de Atleticas').Layout(layout)
