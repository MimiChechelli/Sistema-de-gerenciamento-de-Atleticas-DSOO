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

    # def pegar_codigo_partida(self):
    #     codigo = int(input(" Insira o código da partida: "))
    #     print("\n")
    #     return codigo

    def pegar_dados_partida(self, lista_atleticas, lista_arbitros):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS PARTIDA ---------', font=("Helvica", 25))],
            [sg.Text('Insira o código da partida: ', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Data da partida: ', size=(15, 1)), sg.InputText('', key='data_partida')],
            [sg.Text('Selecione a primeira atlética: ')],
            [sg.Listbox(values=lista_atleticas, size=(30, 6), key='atletica_1')],
            [sg.Text('Selecione a segunda atlética: ')],
            [sg.Listbox(values=lista_atleticas, size=(30, 6), key='atletica_2')],
            [sg.Text('Selecione o arbitro da partida: ')],
            [sg.Listbox(values=lista_arbitros, size=(30, 6), key='arbitro')],
            [sg.Text('Insira a pontuação da primeira atlética: ', size=(15, 1)), sg.InputText('', key='resultado_atl_1')],
            [sg.Text('Insira a pontuação da segunda atlética: ', size=(15, 1)), sg.InputText('', key='resultado_atl_1')],
        ]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        codigo = values['codigo']
        data_partida = values['data_partida']
        atletica_1 = values['atletica_1']
        atletica_2 = values['atletica_2']
        arbitro = values['arbitro']
        resultado_atl_1 = values['resultado_atl_1']
        resultado_atl_2 = values['resultado_atl_2']
        self.close()
        return {"codigo": codigo, 
                "data_partida": data_partida, 
                "atletica_1": atletica_1,
                "atletica_2": atletica_2, 
                "arbitro": arbitro, 
                "resultado_atl_1": resultado_atl_1,
                "resultado_atl_2": resultado_atl_2}

    # def mostrar_dados_partida(self, dados):
    #     print(" -------- DADOS PARTIDA ----------")
    #     print(" Código: ", dados["codigo"])
    #     print(" Data: ", dados["data_partida"])
    #     print(" Atlética: ", dados["atletica_1"]," VS ", dados["atletica_2"])
    #     print(" Arbitro: ", dados["arbitro"])
    #     print(" Resultado: ", dados["resultado_atl_1"], " a ",dados["resultado_atl_2"])
    #     print("\n")

    def listar_todas_partidas(self,lista_partida):
        cursos = sorted(set(aluno.cpf for aluno in lista_partida))
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

    def mostrar_partida(self,lista_alunos):
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

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
