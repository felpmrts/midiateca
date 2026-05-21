import os
import time
from app.cli import utils

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
                print("Teste 1")
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
                print("Teste 1")
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