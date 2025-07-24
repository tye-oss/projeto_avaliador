from database import Database
import tkinter as tk
from tkinter import simpledialog, messagebox

class LoginSystem:
    def __init__(self):
        self.db = Database()

    def autenticar(self, email, senha_bytes):
        query = """
        SELECT usuarios.nome, papeis.nome AS papel
        FROM usuarios
        JOIN papeis ON usuarios.papel = papeis.id
        WHERE usuarios.email = %s AND usuarios.senha = %s
        """
        resultado = self.db.execute_query(query, (email, senha_bytes), fetch=True)
        return resultado[0] if resultado else None

    def solicitar_login(self):
        root = tk.Tk()
        root.withdraw()

        email = simpledialog.askstring("Login", "Email:")
        senha = simpledialog.askstring("Senha", "Senha:", show='*')

        if not email or not senha:
            messagebox.showerror("Erro", "Email ou senha não fornecidos.")
            return None

        senha_bytes = senha.encode()  # compatível com VARBINARY

        user = self.autenticar(email, senha_bytes)
        if not user:
            messagebox.showerror("Erro", "Credenciais inválidas.")
        return user