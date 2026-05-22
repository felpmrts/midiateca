import sqlite3
from pathlib import Path

class DatabaseManager:
    def __init__(self):
        # 📂 Define onde o arquivo do banco (.db) vai ser salvo automaticamente
        self.caminho_banco = Path(__file__).parent / "tracker_midias.db"
        # 🛠️ Cria a tabela no banco assim que o sistema inicia (se ela não existir)
        self.criar_tabela()

    def conectar(self):
        # 🔌 Abre a conexão com o arquivo do banco de dados
        return sqlite3.connect(self.caminho_banco)

    def criar_tabela(self):
        # 📊 Comando SQL para criar a tabela única que abrigará todas as mídias
        comando_sql = """
        CREATE TABLE IF NOT EXISTS midias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_midia TEXT NOT NULL,         -- 'Livro', 'Filme', 'Serie_Anime', 'Jogo'
            titulo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            status TEXT NOT NULL,
            nota REAL NOT NULL,
            genero TEXT NOT NULL,
            
            -- Campos específicos de cada mídia (podem ser NULL / vazios)
            autor TEXT,                       -- Livros e Séries/Animes
            paginas INTEGER,                  -- Livros
            duracao REAL,                     -- Filmes
            temporadas INTEGER,               -- Séries/Animes
            episodios INTEGER,                -- Séries/Animes
            horas REAL                        -- Jogos
        );
        """
        # Executa o comando e fecha a conexão de forma segura
        with self.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(comando_sql)
            conexao.commit()

    def salvar_midia(self, tipo: str, dados: dict):
        """
        Recebe o tipo da mídia (ex: 'Livro') e o dicionário de dados vindo do formulário,
        e salva diretamente no banco de dados.
        """
        comando_sql = """
        INSERT INTO midias (
            tipo_midia, titulo, ano, status, nota, genero, 
            autor, paginas, duracao, temporadas, episodios, horas
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        
        # Como a tabela é única, extraímos os dados do dicionário usando .get()
        # Se o campo não existir no dicionário (ex: 'horas' em um Livro), o Python envia None (NULL no banco)
        valores = (
            tipo,
            dados.get("titulo"),
            dados.get("ano"),
            dados.get("status"),
            dados.get("nota"),
            dados.get("genero"),
            dados.get("autor"),
            dados.get("paginas"),
            dados.get("duracao"),
            dados.get("temporadas"),
            dados.get("episodios"),
            dados.get("horas")
        )

        with self.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(comando_sql, valores)
            conexao.commit()
    
    def buscar_midias(self, tipo: str = None):
        """
        Busca as mídias no banco. 
        Se passar o tipo (ex: 'Livro'), filtra apenas por ele. 
        Se não passar nada, busca absolutamente tudo.
        """
        with self.conectar() as conexao:
            cursor = conexao.cursor()
            
            if tipo:
                comando_sql = "SELECT * FROM midias WHERE tipo_midia = ?;"
                cursor.execute(comando_sql, (tipo,))
            else:
                comando_sql = "SELECT * FROM midias;"
                cursor.execute(comando_sql)
                
            # fetchall() traz todas as linhas encontradas no banco em formato de lista
            return cursor.fetchall()