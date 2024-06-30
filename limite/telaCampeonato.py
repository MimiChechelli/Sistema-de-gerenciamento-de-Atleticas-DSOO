import PySimpleGUI as sg


class TelaCampeonato():
    def __init__(self, controlador_campeonato):
        self.__controlador_campeonato= controlador_campeonato
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- CAMPEONATO ----------', font=("Helvica", 25))],
            [sg.Button('Incluir campeonato',key='1')],
            [sg.Button('Excluir campeonato',key='2')],
            [sg.Button('Incluir partida',key='3')],
            [sg.Button('Excluir partida',key='4')],
            [sg.Button('Listar partidas', key='5')],
            [sg.Button('Ver podio', key='6')],
            [sg.Button('Retornar', key='0')]
        ]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        self.close()
        return int(button)

    def mostrar_campeonatos(self, lista_campeonatos):
        edicao = sorted(set(campeonato.edicao for campeonato in lista_campeonatos))
        layout_curso = [
            [sg.Text('Selecione a edição do campeonato desejado: ')],
            [sg.Listbox(values=edicao, size=(30, 6), key='campeonato_selecionado')],
            [sg.Button('Selecionar campeonato')]
        ]
        window = sg.Window('Seleção de campeonato').Layout(layout_curso)
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED:
            window.close()
            return None
        campeonato_selecionado = valores['campeonato_selecionado'][0] if valores['campeonato_selecionado'] else None
        window.close()
        if not campeonato_selecionado:
            return None
        return campeonato_selecionado

    # def pegar_dados_campeonato(self):
    #     print(" -------- DADOS CAMPEONATO ----------")
    #     edicao = int(input(" Edição do campeonato: "))
    #     print("\n")
    #     return edicao

    # def lista_edicoes(self, campeonatos):
    #     for campeonato in campeonatos:
    #         print(campeonato.edicao)

    # def pega_edicao(self):
    #     edicao = int(input("Qual Edição? "))
    #     print("\n")
    #     return edicao

    # def mostrar_dados_campeonato(self, dados):
    #     print(" -------- DADOS CAMPEONATO ----------")
    #     print(" Código: ", dados["codigo"])
    #     print(" Edição do campeonato: ", dados["edicao"])
    #     print(" Pontuações: ", end="")
    #     for atletica, pontuacao in dados["pontuacao"]:
    #         print(f"Atlética: {atletica}, pontuação: {pontuacao}", end=", ")
    #     print(" Partidas: ", end="")
    #     for elemento in dados["partidas"]:
    #         print(elemento, end=", ")
    #     print("\n")

    def mostrar_ranking_campeonato(self, podio: list):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [[sg.Text(f'-------- Podio ----------', font=("Helvica", 25))],
                    [sg.Text(f'Primeiro lugar: {podio[0]}', font=("Helvica", 25))],
                    [sg.Text(f'Segundo lugar: {podio[1]}', font=("Helvica", 25))],
                    [sg.Text(f'Terceiro lugar: {podio[2]}', font=("Helvica", 25))]]
        self.__window = sg.Window('Sistema de atlética').Layout(layout)
        button, values = self.open()
        self.close()

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
