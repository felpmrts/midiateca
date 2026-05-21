import os
import time
from app.cli import utils
from app.cli import formularios
from app.core import models

def menu():

    option = 10 #iniciar a variavel

    while option != 0:

        utils.clear_screen()

        print(f"========= Menu =========\n")
        print("1. Adicionar Nova Mídia")
        print("2. Modificar Mídia")
        print("3. Remover Mídia")
        print("4. Vizualizar Mídias")
        print("0. Sair")

        try:
            option = int(input(">> "))
        except ValueError:
            utils.clear_screen()
            print("Entrada inválida: digite um número inteiro.")
            time.sleep(2)
            continue

        match option:
            case 0:
                pass
            case 1:
                utils.clear_screen()
                print("=== O que deseja adicionar? ===")
                print("1. Livro")
                print("2. Filme")
                print("3. Serie/Anime")
                print("4. Jogo")
                print("0. Voltar")

                try:
                    suboption = int(input(">> "))
                except ValueError:
                    print("Opção inválida! Tente novamente")
                    time.sleep(2)
                    continue

                match suboption:
                    case 0:
                        pass
                    case 1:
                        
                        dados_livro = formularios.obter_dados_livro()

                        if dados_livro:

                            novo_livro = models.Livro(
                                titulo=dados_livro["titulo"],
                                ano=dados_livro["ano"],
                                status=dados_livro["status"],
                                nota=dados_livro["nota"],
                                genero=dados_livro["genero"],
                                autor=dados_livro["autor"],
                                paginas=dados_livro["paginas"]
                            )

                            print(f"Objeto {novo_livro} criado com sucesso!")
                            time.sleep(2)

                    case 2:
                        
                        dados_filme = formularios.obter_dados_filme()

                        if dados_filme:

                            novo_filme = models.Filme(
                                titulo=dados_filme["titulo"],
                                ano=dados_filme["ano"],
                                status=dados_filme["status"],
                                nota=dados_filme["nota"],
                                genero=dados_filme["genero"],
                                duracao=dados_filme["duracao"]
                            )

                            print(f"Objeto {novo_filme} criado com sucesso!")
                            time.sleep(2)
                    case 3:
                        
                        dados_serie_anime = formularios.obter_dados_serie_anime()

                        if dados_serie_anime:

                            nova_serie_anime = models.Serie_Anime(
                                titulo=dados_serie_anime["titulo"],
                                ano=dados_serie_anime["ano"],
                                status=dados_serie_anime["status"],
                                nota=dados_serie_anime["nota"],
                                genero=dados_serie_anime["genero"],
                                temporadas=dados_serie_anime["temporadas"],
                                episodios=dados_serie_anime["episodios"],
                                autor=dados_serie_anime["autor"]
                            )

                            print(f"Objeto {nova_serie_anime} criado com sucesso!")
                            time.sleep(2)
                    case 4:
                        
                        dados_jogo = formularios.obter_dados_jogo()

                        if dados_jogo:

                            novo_jogo = models.Jogo(
                                titulo=dados_jogo["titulo"],
                                ano=dados_jogo["ano"],
                                status=dados_jogo["status"],
                                nota=dados_jogo["nota"],
                                genero=dados_jogo["genero"],
                                horas=dados_jogo["horas"]
                            )

                            print(f"Objeto {novo_jogo} criado com sucesso!")
                            time.sleep(2)
                    case _:
                        print("Opção inválida. Tente novamente")
                        time.sleep(2)
            
            case 2:
                print("Teste 2")
            case 3:
                print("teste 3")
            case 4:
                submenu_opcao_quatro()
            case _:
                print("Opção invalida")

def submenu_opcao_quatro():
    
    option = 10

    while option != 0:

        utils.clear_screen()

        print(f"==== Visualizar Mídias ====\n")
        print("1. Ver Tudo")
        print("2. Apenas Filmes")
        print("3. Apenas Séries/Animes")
        print("4. Apenas Livros")
        print("5. Apenas Jogos")
        print("0. Voltar")

        try:
            option = int(input(">> "))
        except ValueError:
            utils.clear_screen()
            print("Entrada inválida: digite um número inteiro.")
            time.sleep(2)
            continue

        match option:
            case 0:
                pass
            case 1:
                pass
            case 2:
                print("Teste 2")
            case 3:
                print("teste 3")
            case 4:
                print("teste 4")
            case 5:
                print("teste 5")
            case _:
                print("Opção invalida")