import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

class Backend:
    def __init__(self):
        print("🔐 Conectando ao banco via .env...")
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.conn.cursor()
        
        
    def adicionar_produto(self, nome, qtd, preco):
        query = "INSERT INTO produtos (nome, quantidade, preco) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE quantidade=quantidade+%s, preco=%s"
        self.cursor.execute(query, (nome, qtd, preco, qtd, preco))
        self.conn.commit()

    def remover_produto(self, nome):
        query = "DELETE FROM produtos WHERE nome = %s"
        self.cursor.execute(query, (nome,))
        self.conn.commit()

    def listar_produtos(self):
        self.cursor.execute("SELECT nome, quantidade, preco FROM produtos")
        return self.cursor.fetchall()

    def fechar(self):
        self.conn.close()