


class TelaCampeonato():
    def tela_opcoes(self):
        print("┏━━━━━━━━━━━━━━━━━┓")
        print(" -------- CAMPEONATO ----------")
        print(" Escolha a opcao")
        print(" 1 - Incluir campeonato")
        print(" 2 - Visualizar campeonato")
        print(" 3 - Listar campeonato")
        print(" 4 - Excluir campeonato")
        print(" 0 - Retornar")
        opcao = int(input(" Escolha a opção: "))
        print("┗━━━━━━━━━━━━━━━━━┛")
        print("\n")
        return opcao

    def pegar_dados_campeonato(self):
        print("┏━━━━━━━━━━━━━━━━━┓")
        print(" -------- DADOS CAMPEONATO ----------")
        edicao = input(" Edição do campeonato: ")
        print("┗━━━━━━━━━━━━━━━━━┛")
        print("\n")
        return { "edicao":{edicao}}

    def mostrar_dados_campeonato(self, dados):
        print("┏━━━━━━━━━━━━━━━━━┓")
        print(" -------- DADOS CAMPEONATO ----------")
        print(" Edição do campeonato: ", dados["edicao"])
        print(" Pontuações: ", end="")
        for atletica, pontuacao in dados["pontuacao"]:
            print(f"Atlética: {atletica}, pontuação: {pontuacao}", end=", ")
        print(" Partidas: ", end="")
        for elemento in dados["partidas"]:
            print(elemento, end=", ")
        print("┗━━━━━━━━━━━━━━━━━┛")
        print("\n")

    def mostrar_ranking_campeonato(self):
        pass
