import PySimpleGUI as sg


class TelaPartida():
    def __init__(self, controlador_partida):
        self.__controlador_partida = controlador_partida
        self.__window = None


    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- PARTIDA ----------', font=("Helvica", 25))],
            [sg.Button('Incluir partida',key='1')],
            [sg.Button('Alterar partida',key='2')],
            [sg.Button('Excluir partida',key='3')],
            [sg.Button('Listar partidas',key='4')],
            [sg.Button('Retornar', key='0')]
        ]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        self.close()
        return int(button)

    def pegar_codigo_partida(self):
        codigo = int(input(" Insira o código da partida: "))
        print("\n")
        return codigo

    def pegar_dados_partida(self):
        print(" -------- DADOS PARTIDA ----------")
        codigo = int(input(" Insira o código da partida: "))
        data_partida = input(" Data da partida: ")
        atletica_1 = input(" Insira a primeira atlética: ")
        atletica_2 = input(" Insira a segunda atlética: ")
        arbitro = input(" Insira o arbitro da partida: ")
        resultado_atl_1 = int(input(" Insira a pontuação da primeira atlética: "))
        resultado_atl_2 = int(input(" Insira a pontuação da segunda atlética: "))
        print("\n")
        return codigo, data_partida, atletica_1, atletica_2, arbitro, resultado_atl_1, resultado_atl_2

    def mostrar_dados_partida(self, dados):
        print(" -------- DADOS PARTIDA ----------")
        print(" Código: ", dados["codigo"])
        print(" Data: ", dados["data_partida"])
        print(" Atlética: ", dados["atletica_1"]," VS ", dados["atletica_2"])
        print(" Arbitro: ", dados["arbitro"])
        print(" Resultado: ", dados["resultado_atl_1"], " a ",dados["resultado_atl_2"])
        print("\n")

    # def mostrar_alunos(self,lista_alunos):
    #     cursos = sorted(set(aluno.cpf for aluno in lista_alunos))
    #     layout_curso = [
    #         [sg.Text('Selecione o CPF do aluno')],
    #         [sg.Listbox(values=cursos, size=(30, 6), key='aluno_selecionado')],
    #         [sg.Button('Selecionar aluno')]
    #     ]
    #     window = sg.Window('Seleção de Aluno').Layout(layout_curso)
    #     evento, valores = window.read()
    #     if evento == sg.WIN_CLOSED:
    #         window.close()
    #         return None
    #     aluno_selecionado = valores['aluno_selecionado'][0] if valores['aluno_selecionado'] else None
    #     window.close()
    #     if not aluno_selecionado:
    #         return None
    #     return aluno_selecionado

    def mostra_mensagem(self, msg):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [[sg.Text(f'{msg}', font=("Helvica", 25))]]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        self.close()

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
