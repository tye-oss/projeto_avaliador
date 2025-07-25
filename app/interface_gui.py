import tkinter as tk
from tkinter import messagebox
from backend_mysql import Backend

class EstoqueGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📦 Gerenciador de Estoque")
        self.root.geometry("420x480")
        self.root.configure(bg="#f9f9f9")
        self.root.protocol("WM_DELETE_WINDOW", self.sair)

        # Backend
        try:
            self.db = Backend()
        except Exception as e:
            print("⚠️ Erro ao iniciar backend:", e)
            self.db = None

        # Fontes padrão
        fonte = ("Segoe UI", 10)

        # Campos de entrada
        tk.Label(root, text="Produto:", font=fonte, bg="#f9f9f9").pack()
        self.entry_nome = tk.Entry(root, font=fonte)
        self.entry_nome.pack(pady=2)

        tk.Label(root, text="Quantidade:", font=fonte, bg="#f9f9f9").pack()
        self.entry_qtd = tk.Entry(root, font=fonte)
        self.entry_qtd.pack(pady=2)

        tk.Label(root, text="Preço:", font=fonte, bg="#f9f9f9").pack()
        self.entry_preco = tk.Entry(root, font=fonte)
        self.entry_preco.pack(pady=2)

        # Botões de ação
        btn_frame = tk.Frame(root, bg="#f9f9f9")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="➕ Adicionar Produto", command=self.adicionar_produto, width=20).pack(pady=2)
        tk.Button(btn_frame, text="➖ Remover Produto", command=self.remover_produto, width=20).pack(pady=2)
        tk.Button(btn_frame, text="📋 Mostrar Estoque", command=self.mostrar_estoque, width=20).pack(pady=2)
        tk.Button(btn_frame, text="🧾 Abrir Caixa", command=self.abrir_caixa, width=20).pack(pady=2)
        tk.Button(btn_frame, text="❌ Sair", command=self.sair, fg="red", width=20).pack(pady=10)

        # Área de exibição
        self.texto = tk.Text(root, height=12, width=48)
        self.texto.pack(pady=10)

    def adicionar_produto(self):
        nome = self.entry_nome.get().strip().lower()
        try:
            qtd = int(self.entry_qtd.get())
            preco = float(self.entry_preco.get())
            self.db.adicionar_produto(nome, qtd, preco)
            messagebox.showinfo("Sucesso", f"{nome} adicionado!")
            self.limpar_campos()
        except ValueError:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente!")

    def remover_produto(self):
        nome = self.entry_nome.get().strip().lower()
        self.db.remover_produto(nome)
        messagebox.showinfo("Removido", f"{nome} removido do estoque.")
        self.limpar_campos()

    def mostrar_estoque(self):
        self.texto.delete("1.0", tk.END)
        produtos = self.db.listar_produtos()
        if not produtos:
            self.texto.insert(tk.END, "Estoque vazio.\n")
        else:
            for nome, qtd, preco in produtos:
                self.texto.insert(tk.END, f"{nome.title()} — {qtd} unidades — R$ {preco:.2f}\n")

    def abrir_caixa(self):
        messagebox.showinfo("Caixa", "Função ainda em construção. 😉")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_qtd.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def sair(self):
        self.db.fechar()
        self.root.destroy()