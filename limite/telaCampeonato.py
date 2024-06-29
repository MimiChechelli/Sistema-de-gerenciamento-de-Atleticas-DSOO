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

    def pegar_dados_campeonato(self):
        print(" -------- DADOS CAMPEONATO ----------")
        edicao = int(input(" Edição do campeonato: "))
        print("\n")
        return edicao

    def lista_edicoes(self, campeonatos):
        for campeonato in campeonatos:
            print(campeonato.edicao)


    def pega_edicao(self):
        edicao = int(input("Qual Edição? "))
        print("\n")
        return edicao

    def mostrar_dados_campeonato(self, dados):
        print(" -------- DADOS CAMPEONATO ----------")
        print(" Código: ", dados["codigo"])
        print(" Edição do campeonato: ", dados["edicao"])
        print(" Pontuações: ", end="")
        for atletica, pontuacao in dados["pontuacao"]:
            print(f"Atlética: {atletica}, pontuação: {pontuacao}", end=", ")
        print(" Partidas: ", end="")
        for elemento in dados["partidas"]:
            print(elemento, end=", ")
        print("\n")

    def mostrar_ranking_campeonato(self, podio: list):
        print("Primeiro:", podio[0], "Segundo:", podio[1], "e Terceiro:", podio[2])
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
