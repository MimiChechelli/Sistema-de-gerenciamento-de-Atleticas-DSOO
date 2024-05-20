


class TelaCampeonato():
    def tela_opcoes(self):
        print(" -------- CAMPEONATO ----------")
        print(" Escolha a opcao")
        print(" 1 - Incluir campeonato")
        print(" 2 - Excluir campeonato")
        print(" 3 - Incluir partida")
        print(" 4 - Excluir partida")
        print(" 5 - Listar partidas")
        print(" 6 - Ver podio")
        print(" 0 - Retornar")
        opcao = int(input(" Escolha a opção: "))
        print("\n")
        return opcao

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
            print(f"Atlética: atletica, pontuação: pontuacao", end=", ")
        print(" Partidas: ", end="")
        for elemento in dados["partidas"]:
            print(elemento, end=", ")
        print("\n")

    def mostrar_ranking_campeonato(self, podio: list):
        print("Primeiro:", podio[0], "Segundo:", podio[1], "e Terceiro:", podio[2])
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)