import PySimpleGUI as sg


class TelaPartida():
    def __init__(self, controlador_partida):
        self.__controlador_partida = controlador_partida
        self.__window = None


    def tela_opcoes(self):
        print(" -------- PARTIDA ----------")
        print(" Escolha a opcao")
        print(" 1 - Incluir partida")
        print(" 2 - Alterar partida")
        print(" 3 - Excluir partida")
        print(" 4 - Listar partidas")
        print(" 0 - Retornar")
        opcao = int(input(" Escolha a opção: "))
        print("\n")
        return opcao

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

    def mostra_mensagem(self, msg):
        print(msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
