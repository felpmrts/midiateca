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

                            print(f"\nLivro salvo no banco com sucesso!")
                            time.sleep(2)

                    case 2:

                        dados_filme = formularios.obter_dados_filme()
                        
                        if dados_filme:
                            db.salvar_midia("Filme", dados_filme)

                            print(f"\nFilme salvo no banco com sucesso!")
                            time.sleep(2)

                    case 3:
                        
                        dados_serie_anime = formularios.obter_dados_serie_anime()

                        if dados_serie_anime:
                            db.salvar_midia("Serie/Anime", dados_serie_anime)

                            print(f"\nSérie/Anime salvo no banco com sucesso!")
                            time.sleep(2)
                    case 4:
                        
                        dados_jogo = formularios.obter_dados_jogo()

                        if dados_jogo:

                            db.salvar_midia("Jogo", dados_jogo)

                            print(f"\nJogo salvo no banco com sucesso!")
                            time.sleep(2)

                    case _:
                        print("Opção inválida. Tente novamente")
                        time.sleep(2)
            
            case 2:
                submenu_modificar_midia(db)
            case 3:
                submenu_remover_midia(db)
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
                        print(f"{i}. {filme[2]} | Nota: {filme[5]} ⭐ | Gênero: {filme[6]} | Ano: {filme[3]} | Duração: {filme[9]}h")
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
                        print(f"{i}. {serie[2]} | Nota: {serie[5]} ⭐ | Gênero: {serie[6]} | Temporadas: {serie[10]} | Episódios: {serie[11]} | Ano: {serie[3]} | Autor/Diretor: {serie[7]}")
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
                        print(f"{i}. {livro[2]} | Nota: {livro[5]} ⭐ | Gênero: {livro[6]} | Autor: {livro[7]} | Páginas: {livro[8]} | Ano: {livro[3]}")
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
                        print(f"{i}. {jogo[2]} | Nota: {jogo[5]} ⭐ | Gênero: {jogo[6]} | Ano: {jogo[3]} | Horas: {jogo[12]}h")
                        i += 1
                input("\nPressione Enter para voltar...")

            case _:
                print("Opção inválida")
                time.sleep(2)

def submenu_modificar_midia(db):

    option = 10

    while option != 0:

        utils.clear_screen()

        print(f"==== Modificar Mídia ====\n")
        print("1. Filmes")
        print("2. Séries/Animes")
        print("3. Livros")
        print("4. Jogos")
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
                print("=== Selecione um Filme para Modificar ===\n")
                filmes = db.buscar_midias("Filme")

                if not filmes:
                    print("Nenhum filme cadastrado ainda.")
                    input("\nPressione Enter para voltar...")
                else:
                    for i, filme in enumerate(filmes, 1):
                        print(f"{i}. {filme[2]} | Ano: {filme[3]} | Nota: {filme[5]} ⭐")

                    try:
                        escolha = int(input("\nEscolha o número do filme: "))
                        if 1 <= escolha <= len(filmes):
                            midia_id = filmes[escolha - 1][0]
                            dados_atuais = {
                                "titulo": filmes[escolha - 1][2],
                                "ano": filmes[escolha - 1][3],
                                "status": filmes[escolha - 1][4],
                                "nota": filmes[escolha - 1][5],
                                "genero": filmes[escolha - 1][6],
                                "duracao": filmes[escolha - 1][9]
                            }

                            dados_editados = formularios.editar_filme(dados_atuais)
                            if dados_editados:
                                db.atualizar_midia(midia_id, "Filme", dados_editados)
                                print("\nFilme atualizado com sucesso!")
                                time.sleep(2)
                        else:
                            print("Opção inválida!")
                            time.sleep(2)
                    except ValueError:
                        print("Digite um número válido!")
                        time.sleep(2)

            case 2:
                utils.clear_screen()
                print("=== Selecione uma Série/Anime para Modificar ===\n")
                series = db.buscar_midias("Serie/Anime")

                if not series:
                    print("Nenhuma série/anime cadastrada ainda.")
                    input("\nPressione Enter para voltar...")
                else:
                    for i, serie in enumerate(series, 1):
                        print(f"{i}. {serie[2]} | Ano: {serie[3]} | Nota: {serie[5]} ⭐")

                    try:
                        escolha = int(input("\nEscolha o número da série/anime: "))
                        if 1 <= escolha <= len(series):
                            midia_id = series[escolha - 1][0]
                            dados_atuais = {
                                "titulo": series[escolha - 1][2],
                                "ano": series[escolha - 1][3],
                                "status": series[escolha - 1][4],
                                "nota": series[escolha - 1][5],
                                "genero": series[escolha - 1][6],
                                "autor": series[escolha - 1][7],
                                "temporadas": series[escolha - 1][10],
                                "episodios": series[escolha - 1][11]
                            }

                            dados_editados = formularios.editar_serie_anime(dados_atuais)
                            if dados_editados:
                                db.atualizar_midia(midia_id, "Serie/Anime", dados_editados)
                                print("\nSérie/Anime atualizada com sucesso!")
                                time.sleep(2)
                        else:
                            print("Opção inválida!")
                            time.sleep(2)
                    except ValueError:
                        print("Digite um número válido!")
                        time.sleep(2)

            case 3:
                utils.clear_screen()
                print("=== Selecione um Livro para Modificar ===\n")
                livros = db.buscar_midias("Livro")

                if not livros:
                    print("Nenhum livro cadastrado ainda.")
                    input("\nPressione Enter para voltar...")
                else:
                    for i, livro in enumerate(livros, 1):
                        print(f"{i}. {livro[2]} | Ano: {livro[3]} | Nota: {livro[5]} ⭐")

                    try:
                        escolha = int(input("\nEscolha o número do livro: "))
                        if 1 <= escolha <= len(livros):
                            midia_id = livros[escolha - 1][0]
                            dados_atuais = {
                                "titulo": livros[escolha - 1][2],
                                "ano": livros[escolha - 1][3],
                                "status": livros[escolha - 1][4],
                                "nota": livros[escolha - 1][5],
                                "genero": livros[escolha - 1][6],
                                "autor": livros[escolha - 1][7],
                                "paginas": livros[escolha - 1][8]
                            }

                            dados_editados = formularios.editar_livro(dados_atuais)
                            if dados_editados:
                                db.atualizar_midia(midia_id, "Livro", dados_editados)
                                print("\nLivro atualizado com sucesso!")
                                time.sleep(2)
                        else:
                            print("Opção inválida!")
                            time.sleep(2)
                    except ValueError:
                        print("Digite um número válido!")
                        time.sleep(2)

            case 4:
                utils.clear_screen()
                print("=== Selecione um Jogo para Modificar ===\n")
                jogos = db.buscar_midias("Jogo")

                if not jogos:
                    print("Nenhum jogo cadastrado ainda.")
                    input("\nPressione Enter para voltar...")
                else:
                    for i, jogo in enumerate(jogos, 1):
                        print(f"{i}. {jogo[2]} | Ano: {jogo[3]} | Nota: {jogo[5]} ⭐")

                    try:
                        escolha = int(input("\nEscolha o número do jogo: "))
                        if 1 <= escolha <= len(jogos):
                            midia_id = jogos[escolha - 1][0]
                            dados_atuais = {
                                "titulo": jogos[escolha - 1][2],
                                "ano": jogos[escolha - 1][3],
                                "status": jogos[escolha - 1][4],
                                "nota": jogos[escolha - 1][5],
                                "genero": jogos[escolha - 1][6],
                                "horas": jogos[escolha - 1][12]
                            }

                            dados_editados = formularios.editar_jogo(dados_atuais)
                            if dados_editados:
                                db.atualizar_midia(midia_id, "Jogo", dados_editados)
                                print("\nJogo atualizado com sucesso!")
                                time.sleep(2)
                        else:
                            print("Opção inválida!")
                            time.sleep(2)
                    except ValueError:
                        print("Digite um número válido!")
                        time.sleep(2)

            case _:
                print("Opção inválida")
                time.sleep(2)

def submenu_remover_midia(db):

    option = 10

    while option != 0:

        utils.clear_screen()

        print(f"==== Remover Mídia ====\n")
        print("1. Filmes")
        print("2. Séries/Animes")
        print("3. Livros")
        print("4. Jogos")
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
                print("=== Selecione um Filme para Remover ===\n")
                filmes = db.buscar_midias("Filme")

                if not filmes:
                    print("Nenhum filme cadastrado ainda.")
                    input("\nPressione Enter para voltar...")
                else:
                    for i, filme in enumerate(filmes, 1):
                        print(f"{i}. {filme[2]} | Ano: {filme[3]} | Nota: {filme[5]} ⭐")

                    try:
                        escolha = int(input("\nEscolha o número do filme: "))
                        if 1 <= escolha <= len(filmes):
                            midia_id = filmes[escolha - 1][0]
                            confirmacao = input(f"\nTem certeza que deseja remover '{filmes[escolha - 1][2]}'? (s/n): ").lower()
                            if confirmacao == 's':
                                db.deletar_midia(midia_id)
                                print("Filme removido com sucesso!")
                                time.sleep(2)
                            else:
                                print("Remoção cancelada!")
                                time.sleep(1)
                        else:
                            print("Opção inválida!")
                            time.sleep(2)
                    except ValueError:
                        print("Digite um número válido!")
                        time.sleep(2)

            case 2:
                utils.clear_screen()
                print("=== Selecione uma Série/Anime para Remover ===\n")
                series = db.buscar_midias("Serie/Anime")

                if not series:
                    print("Nenhuma série/anime cadastrada ainda.")
                    input("\nPressione Enter para voltar...")
                else:
                    for i, serie in enumerate(series, 1):
                        print(f"{i}. {serie[2]} | Ano: {serie[3]} | Nota: {serie[5]} ⭐")

                    try:
                        escolha = int(input("\nEscolha o número da série/anime: "))
                        if 1 <= escolha <= len(series):
                            midia_id = series[escolha - 1][0]
                            confirmacao = input(f"\nTem certeza que deseja remover '{series[escolha - 1][2]}'? (s/n): ").lower()
                            if confirmacao == 's':
                                db.deletar_midia(midia_id)
                                print("Série/Anime removida com sucesso!")
                                time.sleep(2)
                            else:
                                print("Remoção cancelada!")
                                time.sleep(1)
                        else:
                            print("Opção inválida!")
                            time.sleep(2)
                    except ValueError:
                        print("Digite um número válido!")
                        time.sleep(2)

            case 3:
                utils.clear_screen()
                print("=== Selecione um Livro para Remover ===\n")
                livros = db.buscar_midias("Livro")

                if not livros:
                    print("Nenhum livro cadastrado ainda.")
                    input("\nPressione Enter para voltar...")
                else:
                    for i, livro in enumerate(livros, 1):
                        print(f"{i}. {livro[2]} | Ano: {livro[3]} | Nota: {livro[5]} ⭐")

                    try:
                        escolha = int(input("\nEscolha o número do livro: "))
                        if 1 <= escolha <= len(livros):
                            midia_id = livros[escolha - 1][0]
                            confirmacao = input(f"\nTem certeza que deseja remover '{livros[escolha - 1][2]}'? (s/n): ").lower()
                            if confirmacao == 's':
                                db.deletar_midia(midia_id)
                                print("Livro removido com sucesso!")
                                time.sleep(2)
                            else:
                                print("Remoção cancelada!")
                                time.sleep(1)
                        else:
                            print("Opção inválida!")
                            time.sleep(2)
                    except ValueError:
                        print("Digite um número válido!")
                        time.sleep(2)

            case 4:
                utils.clear_screen()
                print("=== Selecione um Jogo para Remover ===\n")
                jogos = db.buscar_midias("Jogo")

                if not jogos:
                    print("Nenhum jogo cadastrado ainda.")
                    input("\nPressione Enter para voltar...")
                else:
                    for i, jogo in enumerate(jogos, 1):
                        print(f"{i}. {jogo[2]} | Ano: {jogo[3]} | Nota: {jogo[5]} ⭐")

                    try:
                        escolha = int(input("\nEscolha o número do jogo: "))
                        if 1 <= escolha <= len(jogos):
                            midia_id = jogos[escolha - 1][0]
                            confirmacao = input(f"\nTem certeza que deseja remover '{jogos[escolha - 1][2]}'? (s/n): ").lower()
                            if confirmacao == 's':
                                db.deletar_midia(midia_id)
                                print("Jogo removido com sucesso!")
                                time.sleep(2)
                            else:
                                print("Remoção cancelada!")
                                time.sleep(1)
                        else:
                            print("Opção inválida!")
                            time.sleep(2)
                    except ValueError:
                        print("Digite um número válido!")
                        time.sleep(2)

            case _:
                print("Opção inválida")
                time.sleep(2)