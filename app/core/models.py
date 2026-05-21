
class Midia:

    def __init__(self, titulo: str, ano: int, status: str, nota: float, genero: str):
        self.__titulo = titulo
        self.__ano = ano
        self.__status = status
        self.__nota = nota
        self.__genero = genero

class Livro(Midia):

    def __init__(self, titulo, ano, status, nota, genero, autor, paginas):
        super().__init__(titulo, ano, status, nota, genero)
        self.__autor = autor
        self.__paginas = paginas

class Filme(Midia):

    def __init__(self, titulo, ano, status, nota, genero, duracao):
        super().__init__(titulo, ano, status, nota, genero)
        self.__duracao = duracao

class Serie_Anime(Midia):

    def __init__(self, titulo, ano, status, nota, genero, temporadas, episodios, autor):
        super().__init__(titulo, ano, status, nota, genero)
        self.__temporadas = temporadas
        self.__episodios = episodios
        self.__autor = autor

class Jogo(Midia):

    def __init__(self, titulo, ano, status, nota, genero, horas):
        super().__init__(titulo, ano, status, nota, genero)
        self.__horas = horas
