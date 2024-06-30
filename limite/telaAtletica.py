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

    def mostrar_atleticas(self,lista_atleticas):
        cursos = sorted(set(atletica.curso for atletica in lista_atleticas))
        layout_curso = [
            [sg.Text('Selecione o Curso')],
            [sg.Listbox(values=cursos, size=(30, 6), key='curso_selecionado')],
            [sg.Button('Selecionar Curso')]
        ]
        window = sg.Window('Seleção de Curso').Layout(layout_curso)
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED:
            window.close()
            return None
        curso_selecionado = valores['curso_selecionado'][0] if valores['curso_selecionado'] else None
        window.close()
        if not curso_selecionado:
            return None
        return curso_selecionado

    def mostra_mensagem(self, msg):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [[sg.Text(f'{msg}', font=("Helvica", 25))]]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        self.close()

