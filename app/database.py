import mysql.connector
from app.config import Config
import logging

# Configuração do logger
logging.basicConfig(filename='pyonerp.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Database:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
                port=Config.DB_PORT
            )
            logging.info("Conexão com o banco de dados estabelecida.")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao conectar ao banco: {err}")
            raise

    def execute_query(self, query, params=None, fetch=False):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            if fetch:
                result = cursor.fetchall()
                self.connection.commit()
                return result
            self.connection.commit()
        except mysql.connector.Error as err:
            logging.error(f"Erro ao executar query: {err}")
            raise
        finally:
            cursor.close()

    def close(self):
        if self.connection:
            self.connection.close()
            logging.info("Conexão com o banco de dados fechada.")