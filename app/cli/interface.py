import os
import time
from app.cli import utils
from app.cli import formularios
from app.core import models
from app.database.database import DatabaseManager

def menu():

    #Instanciando banco de dados
    db = DatabaseManager()

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

                            db.salvar_midia("Livro", dados_livro)

                            print("Livro salvo no banco com sucesso!")
                            time.sleep(2)

                    case 2:

                        dados_filme = formularios.obter_dados_filme()
                        
                        if dados_filme:
                            db.salvar_midia("Filme", dados_filme)

                            print("Filme salvo no banco com sucesso!")
                            time.sleep(2)

                    case 3:
                        
                        dados_serie_anime = formularios.obter_dados_serie_anime()

                        if dados_serie_anime:
                            db.salvar_midia("Serie/Anime", dados_serie_anime)

                            print("Série/Anime salvo no banco com sucesso!")
                            time.sleep(2)
                    case 4:
                        
                        dados_jogo = formularios.obter_dados_jogo()

                        if dados_jogo:

                            db.salvar_midia("Jogo", dados_jogo)

                            print("Jogo salvo no banco com sucesso!")
                            time.sleep(2)

                    case _:
                        print("Opção inválida. Tente novamente")
                        time.sleep(2)
            
            case 2:
                print("Teste 2")
            case 3:
                print("teste 3")
            case 4:
                submenu_opcao_quatro(db)
            case _:
                print("Opção invalida")

def submenu_opcao_quatro(db):
    
    option = 10

    while option != 0:

        utils.clear_screen()

        print(f"==== Visualizar Mídias ====\n")
        print("1. Apenas Filmes")
        print("2. Apenas Séries/Animes")
        print("3. Apenas Livros")
        print("4. Apenas Jogos")
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
                utils.clear_screen()
                print("=== Lista de Filmes ===\n")
                filmes = db.buscar_midias("Filme")
                
                if not filmes:
                    print("Nenhum filme cadastrado ainda.")
                else:
                    i = 1  # Iniciado ANTES do loop
                    for filme in filmes:
                        print(f"{i}. {filme[2]} | Status: {filme[4]} | Nota: {filme[5]} ⭐ | Gênero: {filme[6]} | Ano: {filme[3]} | Duração: {filme[9]}h")
                        i += 1
                input("\nPressione Enter para voltar...")

            case 2:
                utils.clear_screen()
                print("=== Lista de Séries/Animes ===\n")
                # Ajustado para "Serie/Anime" para bater com o que foi salvo no case 1
                series = db.buscar_midias("Serie/Anime")
                
                if not series:
                    print("Nenhuma série/anime cadastrada ainda.")
                else:
                    i = 1
                    for serie in series:
                        print(f"{i}. {serie[2]} | Status: {serie[4]} | Nota: {serie[5]} ⭐ | Gênero: {serie[6]} | Temporadas: {serie[10]} | Episódios: {serie[11]} | Ano: {serie[3]} | Autor/Diretor: {serie[7]}")
                        i += 1
                input("\nPressione Enter para voltar...")

            case 3:
                utils.clear_screen()
                print("=== Lista de Livros ===\n")
                # Ajustado para "Livro" no singular
                livros = db.buscar_midias("Livro")
                
                if not livros:
                    print("Nenhum livro cadastrado ainda.")
                else:
                    i = 1
                    for livro in livros:
                        print(f"{i}. {livro[2]} | Status: {livro[4]} | Nota: {livro[5]} ⭐ | Gênero: {livro[6]} | Autor: {livro[7]} | Páginas: {livro[8]} | Ano: {livro[3]}")
                        i += 1
                input("\nPressione Enter para voltar...")

            case 4:
                utils.clear_screen()
                print("=== Lista de Jogos ===\n")
                # Ajustado para "Jogo" no singular
                jogos = db.buscar_midias("Jogo")
                
                if not jogos:
                    print("Nenhum jogo cadastrado ainda.")
                else:
                    i = 1
                    for jogo in jogos:
                        print(f"{i}. {jogo[2]} | Status: {jogo[4]} | Nota: {jogo[5]} ⭐ | Gênero: {jogo[6]} | Ano: {jogo[3]} | Horas: {jogo[12]}h")
                        i += 1
                input("\nPressione Enter para voltar...")

            case _:
                print("Opção inválida")
                time.sleep(2)