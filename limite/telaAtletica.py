import PySimpleGUI as sg


class TelaAtletica():
    def __init__(self, controlador_atletica):
        self.__controlador_atletica = controlador_atletica
        self.__window = None


    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- ATLÉTICA ----------', font=("Helvica", 25))],
            [sg.Button('Incluir Atlética',key='1')],
            [sg.Button('Excluir Atlética',key='2')],
            [sg.Button('Incluir aluno em Atlética',key='3')],
            [sg.Button('Excluir aluno de uma Atlética', key='4')],
            [sg.Button('Listar alunos de uma Atlética', key='5')],
            [sg.Button('Retornar', key='0')]
        ]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        self.close()
        return int(button)


    def pegar_dados_atletica(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- DADOS ATLÉTICA ----------', font=("Helvica", 25))],
        [sg.Text('Nome do curso:', size=(15, 1)), sg.InputText('', key='curso')],
        [sg.Text('Nome da atlética:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        curso = values['curso']
        nome = values['nome']
        self.close()
        return {"curso": curso, "nome": nome}

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostrar_atleticas(self,atleticas):
        print('Ver teste.py')

    # def mostrar_dados_atletica(self, dados):
    #     print(" -------- DADOS ATLÉTICA ----------")
    #     print(" Nome da Atlética: ", dados["nome"])
    #     print(" Nome do Curso: ", dados["curso"])
    #     print(" Participantes: ", end="")
    #     print("Nome: ",end="")
    #     for elemento in dados["alunos"]:
    #         print(elemento.nome, end=", ")
    #     print("\n")

    # def seleciona_atletica(self):
    #     curso = input("Nome do curso da atlética: ")
    #     return curso

    def mostra_mensagem(self, msg):
        print(msg)

