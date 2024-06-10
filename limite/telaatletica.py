import PySimpleGUI as sg


class TelaAtletica():
    def __init__(self, controlador_atletica):
        self.__controlador_atletica = controlador_atletica
        self.__window = None


    def tela_opcoes(self):
        print(" -------- ATLÉTICA ----------")
        print(" Escolha a opcao")
        print(" 1 - Incluir Atlética")
        print(" 2 - Excluir Atlética")
        print(" 3 - Incluir aluno em Atlética")
        print(" 4 - Excluir aluno de uma Atlética")
        print(" 5 - Listar alunos de uma Atlética")
        print(" 0 - Retornar")
        opcao = int(input(" Escolha a opção: "))
        print("\n")
        return opcao

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

    def mostrar_dados_atletica(self, dados):
        print(" -------- DADOS ATLÉTICA ----------")
        print(" Nome da Atlética: ", dados["nome"])
        print(" Nome do Curso: ", dados["curso"])
        print(" Participantes: ", end="")
        print("Nome: ",end="")
        for elemento in dados["alunos"]:
            print(elemento.nome, end=", ")
        print("\n")

    def seleciona_atletica(self):
        curso = input("Nome do curso da atlética: ")
        return curso

    def mostra_mensagem(self, msg):
        print(msg)

