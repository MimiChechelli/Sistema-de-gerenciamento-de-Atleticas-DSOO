


class TelaPartida():
    def tela_opcoes(self):
        print("┏━━━━━━━━━━━━━━━━━┓")
        print(" -------- PARTIDA ----------")
        print(" Escolha a opcao")
        print(" 1 - Incluir partida")
        print(" 2 - Visualizar partida")
        print(" 3 - Listar atléticas participantes")
        print(" 4 - Excluir partida")
        print(" 0 - Retornar")
        opcao = int(input(" Escolha a opção: "))
        print("┗━━━━━━━━━━━━━━━━━┛")
        print("\n")
        return opcao

    def pegar_dados_partida(self):
        print("┏━━━━━━━━━━━━━━━━━┓")
        print(" -------- DADOS PARTIDA ----------")
        data_partida = input(" Data da partida: ")
        atletica_1 = input(" Insira a primeira atlética: ")
        atletica_2 = input(" Insira a segunda atlética: ")
        arbitro = input(" Insira o arbitro da partida: ")
        resultado_atl_1 = input(" Insira a pontuação da primeira atlética: ")
        resultado_atl_2 = input(" Insira a pontuação da segunda atlética: ")
        print("┗━━━━━━━━━━━━━━━━━┛")
        print("\n")
        return { "data_partida":{data_partida}, "atletica_1":{atletica_1}, "atletica_2":{atletica_2}, "arbitro":{arbitro}, "resultado_atl_1":{resultado_atl_1}, "resultado_atl_2":{resultado_atl_2}}

    def mostrar_dados_partida(self, dados):
        print("┏━━━━━━━━━━━━━━━━━┓")
        print(" -------- DADOS PARTIDA ----------")
        print(" Data: ", dados["data_partida"])
        print(" Atlética: ", dados["atletica_1"]," VS ", dados["atletica_2"])
        print(" Arbitro: ", dados["arbitro"])
        print(" Resultado: ", dados["resultado_atl_1"], " a ",dados["resultado_atl_2"])
        print("┗━━━━━━━━━━━━━━━━━┛")
        print("\n")
