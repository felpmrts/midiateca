import time
from app.cli import utils

def obter_dados_livro() -> dict:

    utils.clear_screen()

    print("--- Cadastro de Livro ---")
    
    # Dados básicos de qualquer mídia
    titulo = input("Título do livro: ")
    genero = input("Gênero: ")

    status_usuario = ""
    opcoes_validas = ["lendo", "concluído", "quero ler"]
    while status_usuario not in opcoes_validas:
        status = input("Status (Lendo / Concluído / Quero Ler): ")
        status_usuario = status.lower()

        if status_usuario not in opcoes_validas:
            print("Erro de digitação. Tente novamente")
            time.sleep(1)
            utils.clear_screen()

    # Tratamento para garantir números válidos
    try:
        ano = int(input("Ano de lançamento: "))
        nota = float(input("Nota (0 a 5): "))
        
        # Dados específicos de Livro
        autor = input("Autor do livro: ")
        paginas = int(input("Quantidade de páginas: "))
        
        # Retorna um dicionário com tudo organizado
        return {
            "titulo": titulo,
            "ano": ano,
            "status": status_usuario,
            "nota": nota,
            "genero": genero,
            "autor": autor,
            "paginas": paginas
        }
        
    except ValueError:
        print("Erro: Ano, Nota e Páginas precisam ser valores numéricos!")
        return None

def obter_dados_filme() -> dict:

    utils.clear_screen()

    print("--- Cadastro de Filme ---")
    
    # Dados básicos de qualquer mídia
    titulo = input("Título do filme: ")
    genero = input("Gênero: ")

    status_usuario = ""
    opcoes_validas = ["concluído", "quero ver"]
    while status_usuario not in opcoes_validas:
        status = input("Status (Concluído / Quero Ver): ")
        status_usuario = status.lower()

        if status_usuario not in opcoes_validas:
            print("Erro de digitação. Tente novamente")
            time.sleep(1)
            utils.clear_screen()

    # Tratamento para garantir números válidos
    try:
        ano = int(input("Ano de lançamento: "))
        nota = float(input("Nota (0 a 5): "))
        duracao_horas = float(input("Duração de horas aproximadas do filme: "))

        # Retorna um dicionário com tudo organizado
        return {
            "titulo": titulo,
            "ano": ano,
            "status": status_usuario,
            "nota": nota,
            "genero": genero,
            "duracao": duracao_horas
        }
        
    except ValueError:
        print("Erro: Ano, Nota e Duração precisam ser valores numéricos!")
        return None


def obter_dados_serie_anime() -> dict:

    utils.clear_screen()

    print("--- Cadastro da Série/Anime ---")
    
    # Dados básicos de qualquer mídia
    titulo = input("Título da série/anime: ")
    genero = input("Gênero: ")

    status_usuario = ""
    opcoes_validas = ["assistindo", "concluído", "quero assistir"]
    while status_usuario not in opcoes_validas:
        status = input("Status (Assistindo / Concluído / Quero Assistir): ")
        status_usuario = status.lower()

        if status_usuario not in opcoes_validas:
            print("Erro de digitação. Tente novamente")
            time.sleep(1)
            utils.clear_screen()

    # Dados específicos
    autor = input("Autor da série/anime: ")

    # Tratamento para garantir números válidos
    try:
        ano = int(input("Ano de lançamento: "))
        nota = float(input("Nota (0 a 5): "))
        temporadas = int(input("Quantidade de temporadas: "))
        episodios = int(input("Quantidade de episodios: "))

        # Retorna um dicionário com tudo organizado
        return {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "status": status_usuario,
            "nota": nota,
            "genero": genero,
            "temporadas": temporadas,
            "episodios": episodios
        }
        
    except ValueError:
        print("Erro: Ano, Nota Temporadas e Episódios precisam ser valores numéricos!")
        return None

def obter_dados_jogo() -> dict:

    utils.clear_screen()

    print("--- Cadastro do Jogo ---")
    
    # Dados básicos de qualquer mídia
    titulo = input("Título do Jogo: ")
    genero = input("Gênero: ")

    status_usuario = ""
    opcoes_validas = ["jogando", "concluído", "quero jogar"]
    while status_usuario not in opcoes_validas:
        status = input("Status (Jogando / Concluído / Quero Jogar): ")
        status_usuario = status.lower()

        if status_usuario not in opcoes_validas:
            print("Erro de digitação. Tente novamente")
            time.sleep(1)
            utils.clear_screen()

    # Tratamento para garantir números válidos
    try:
        ano = int(input("Ano de lançamento: "))
        nota = float(input("Nota (0 a 5): "))
        duracao_horas = float(input("Duração de horas aproximadas de jogo: "))

        # Retorna um dicionário com tudo organizado
        return {
            "titulo": titulo,
            "ano": ano,
            "status": status_usuario,
            "nota": nota,
            "genero": genero,
            "horas": duracao_horas
        }
        
    except ValueError:
        print("Erro: Ano, Nota e Duração precisam ser valores numéricos!")
        return None