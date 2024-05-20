


class TelaPartida():
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

    def pegar_dados_partida(self):
        print(" -------- DADOS PARTIDA ----------")
        codigo = input(" Insira o código da partida: ")
        data_partida = input(" Data da partida: ")
        atletica_1 = input(" Insira o nome da primeira atlética: ")
        atletica_2 = input(" Insira o nome da segunda atlética: ")
        arbitro = input(" Insira o arbitro da partida: ")
        resultado_atl_1 = input(" Insira os gols da primeira atlética: ")
        resultado_atl_2 = input(" Insira os gols da segunda atlética: ")
        print("\n")
        return { "codigo":codigo,"data_partida":data_partida, "atletica_1":atletica_1, "atletica_2":atletica_2, "arbitro":arbitro, "resultado_atl_1":resultado_atl_1, "resultado_atl_2":resultado_atl_2}

    def mostrar_dados_partida(self, dados):
        print(" -------- DADOS PARTIDA ----------")
        print(" Data: ", dados["data_partida"])
        print(" Atlética: ", dados["atletica_1"]," VS ", dados["atletica_2"])
        print(" Arbitro: ", dados["arbitro"])
        print(" Resultado: ", dados["resultado_atl_1"], " a ",dados["resultado_atl_2"])
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)