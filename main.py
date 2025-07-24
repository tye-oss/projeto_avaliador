import tkinter as tk
from interface import EstoqueGUI
from login import LoginSystem

if __name__ == "__main__":
    login = LoginSystem()
    usuario = login.solicitar_login()

    if usuario:
        nome = usuario['nome']
        papel = usuario['papel']

        if papel == 'admin':
            root = tk.Tk()
            app = EstoqueGUI(root)
            root.mainloop()
        else:
            tk.Tk().withdraw()
            from tkinter import messagebox
            messagebox.showinfo("Acesso negado", f"Olá {nome}, apenas administradores podem acessar o estoque.")
