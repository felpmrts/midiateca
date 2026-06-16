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
        temporadas = int(input("Quantidade de temporadas ou Arcos: "))
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

def editar_livro(dados_atual: dict) -> dict:
    """
    Permite editar dados de um livro. Se o usuário não preencher um campo, mantém o original.
    """
    utils.clear_screen()
    print("--- Editar Livro ---")
    print("(Deixe em branco para manter o valor atual)\n")

    titulo = input(f"Título [{dados_atual['titulo']}]: ") or dados_atual['titulo']
    genero = input(f"Gênero [{dados_atual['genero']}]: ") or dados_atual['genero']

    status_usuario = ""
    opcoes_validas = ["lendo", "concluído", "quero ler"]
    status_entrada = input(f"Status [{dados_atual['status']}] (Lendo / Concluído / Quero Ler): ").lower()
    status_usuario = status_entrada if status_entrada in opcoes_validas else dados_atual['status']

    try:
        ano = int(input(f"Ano [{dados_atual['ano']}]: ") or dados_atual['ano'])
        nota = float(input(f"Nota [{dados_atual['nota']}]: ") or dados_atual['nota'])
        autor = input(f"Autor [{dados_atual['autor']}]: ") or dados_atual['autor']
        paginas = int(input(f"Páginas [{dados_atual['paginas']}]: ") or dados_atual['paginas'])

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
        print("Erro: Campos numéricos inválidos!")
        return None

def editar_filme(dados_atual: dict) -> dict:
    utils.clear_screen()
    print("--- Editar Filme ---")
    print("(Deixe em branco para manter o valor atual)\n")

    titulo = input(f"Título [{dados_atual['titulo']}]: ") or dados_atual['titulo']
    genero = input(f"Gênero [{dados_atual['genero']}]: ") or dados_atual['genero']

    status_usuario = ""
    opcoes_validas = ["concluído", "quero ver"]
    status_entrada = input(f"Status [{dados_atual['status']}] (Concluído / Quero Ver): ").lower()
    status_usuario = status_entrada if status_entrada in opcoes_validas else dados_atual['status']

    try:
        ano = int(input(f"Ano [{dados_atual['ano']}]: ") or dados_atual['ano'])
        nota = float(input(f"Nota [{dados_atual['nota']}]: ") or dados_atual['nota'])
        duracao = float(input(f"Duração [h] [{dados_atual['duracao']}]: ") or dados_atual['duracao'])

        return {
            "titulo": titulo,
            "ano": ano,
            "status": status_usuario,
            "nota": nota,
            "genero": genero,
            "duracao": duracao
        }
    except ValueError:
        print("Erro: Campos numéricos inválidos!")
        return None

def editar_serie_anime(dados_atual: dict) -> dict:
    utils.clear_screen()
    print("--- Editar Série/Anime ---")
    print("(Deixe em branco para manter o valor atual)\n")

    titulo = input(f"Título [{dados_atual['titulo']}]: ") or dados_atual['titulo']
    genero = input(f"Gênero [{dados_atual['genero']}]: ") or dados_atual['genero']

    status_usuario = ""
    opcoes_validas = ["assistindo", "concluído", "quero assistir"]
    status_entrada = input(f"Status [{dados_atual['status']}] (Assistindo / Concluído / Quero Assistir): ").lower()
    status_usuario = status_entrada if status_entrada in opcoes_validas else dados_atual['status']

    autor = input(f"Autor [{dados_atual['autor']}]: ") or dados_atual['autor']

    try:
        ano = int(input(f"Ano [{dados_atual['ano']}]: ") or dados_atual['ano'])
        nota = float(input(f"Nota [{dados_atual['nota']}]: ") or dados_atual['nota'])
        temporadas = int(input(f"Temporadas [{dados_atual['temporadas']}]: ") or dados_atual['temporadas'])
        episodios = int(input(f"Episódios [{dados_atual['episodios']}]: ") or dados_atual['episodios'])

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
        print("Erro: Campos numéricos inválidos!")
        return None

def editar_jogo(dados_atual: dict) -> dict:
    utils.clear_screen()
    print("--- Editar Jogo ---")
    print("(Deixe em branco para manter o valor atual)\n")

    titulo = input(f"Título [{dados_atual['titulo']}]: ") or dados_atual['titulo']
    genero = input(f"Gênero [{dados_atual['genero']}]: ") or dados_atual['genero']

    status_usuario = ""
    opcoes_validas = ["jogando", "concluído", "quero jogar"]
    status_entrada = input(f"Status [{dados_atual['status']}] (Jogando / Concluído / Quero Jogar): ").lower()
    status_usuario = status_entrada if status_entrada in opcoes_validas else dados_atual['status']

    try:
        ano = int(input(f"Ano [{dados_atual['ano']}]: ") or dados_atual['ano'])
        nota = float(input(f"Nota [{dados_atual['nota']}]: ") or dados_atual['nota'])
        horas = float(input(f"Horas [h] [{dados_atual['horas']}]: ") or dados_atual['horas'])

        return {
            "titulo": titulo,
            "ano": ano,
            "status": status_usuario,
            "nota": nota,
            "genero": genero,
            "horas": horas
        }
    except ValueError:
        print("Erro: Campos numéricos inválidos!")
        return None