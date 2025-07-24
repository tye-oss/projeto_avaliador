from database import Database

class Backend:
    def __init__(self):
        self.db = Database()
        self.criar_tabela()

    def criar_tabela(self):
        query = """
        CREATE TABLE IF NOT EXISTS produtos (
            nome VARCHAR(255) PRIMARY KEY,
            quantidade INT,
            preco DOUBLE
        )
        """
        self.db.execute_query(query)

    def listar_produtos(self):
        query = "SELECT * FROM produtos"
        return self.db.execute_query(query, fetch=True)

    def adicionar_produto(self, nome, quantidade, preco):
        query = """
        INSERT INTO produtos (nome, quantidade, preco)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE quantidade=%s, preco=%s
        """
        self.db.execute_query(query, (nome, quantidade, preco, quantidade, preco))

    def remover_produto(self, nome):
        query = "DELETE FROM produtos WHERE nome = %s"
        self.db.execute_query(query, (nome,))

    def buscar_produto(self, nome):
        query = "SELECT quantidade, preco FROM produtos WHERE nome = %s"
        result = self.db.execute_query(query, (nome,), fetch=True)
        return result[0] if result else None

    def atualizar_quantidade(self, nome, nova_qtd):
        query = "UPDATE produtos SET quantidade = %s WHERE nome = %s"
        self.db.execute_query(query, (nova_qtd, nome))

    def fechar(self):
        self.db.close()