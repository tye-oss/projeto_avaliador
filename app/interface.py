import tkinter as tk
from tkinter import messagebox
from backend_mysql import Backend
from caixa import Caixa

class EstoqueGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Estoque")
        self.root.geometry("400x460")

        self.db = Backend()
        self.caixa = Caixa()

        # Captura o fechamento via “X” da janela
        self.root.protocol("WM_DELETE_WINDOW", self.sair)

        # Nome do produto
        tk.Label(root, text="Produto:").pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        # Quantidade
        tk.Label(root, text="Quantidade:").pack()
        self.entry_qtd = tk.Entry(root)
        self.entry_qtd.pack()

        # Preço
        tk.Label(root, text="Preço:").pack()
        self.entry_preco = tk.Entry(root)
        self.entry_preco.pack()

        # Botões de ação
        tk.Button(root, text="Adicionar Produto", command=self.adicionar_produto).pack(pady=5)
        tk.Button(root, text="Remover Produto", command=self.remover_produto).pack(pady=5)
        tk.Button(root, text="Mostrar Estoque", command=self.mostrar_estoque).pack(pady=5)
        tk.Button(root, text="Abrir Caixa", command=self.abrir_caixa).pack(pady=5)
        tk.Button(root, text="Sair do Programa", command=self.sair, fg="red").pack(pady=5)

        # Área de exibição
        self.texto = tk.Text(root, height=12, width=45)
        self.texto.pack(pady=10)

    def adicionar_produto(self):
        nome = self.entry_nome.get().strip().lower()
        try:
            qtd = int(self.entry_qtd.get())
            preco = float(self.entry_preco.get())
            self.db.adicionar_produto(nome, qtd, preco)
            messagebox.showinfo("Sucesso", f"{nome} adicionado ao estoque!")
            self.limpar_campos()
        except ValueError:
            messagebox.showwarning("Erro", "Insira valores válidos!")

    def remover_produto(self):
        nome = self.entry_nome.get().strip().lower()
        self.db.remover_produto(nome)
        messagebox.showinfo("Removido", f"{nome} foi removido do estoque!")
        self.limpar_campos()

    def mostrar_estoque(self):
        self.texto.delete("1.0", tk.END)
        produtos = self.db.listar_produtos()
        if not produtos:
            self.texto.insert(tk.END, "Estoque vazio.\n")
        else:
            for nome, qtd, preco in produtos:
                self.texto.insert(tk.END, f"{nome} — Qtd: {qtd}, Preço: R$ {preco:.2f}\n")

    def abrir_caixa(self):
        janela = tk.Toplevel(self.root)
        janela.title("Caixa")
        janela.geometry("300x250")

        tk.Label(janela, text="Produto:").pack()
        entry_nome = tk.Entry(janela)
        entry_nome.pack()

        tk.Label(janela, text="Quantidade:").pack()
        entry_qtd = tk.Entry(janela)
        entry_qtd.pack()

        tk.Label(janela, text="Valor Pago: R$").pack()
        entry_pago = tk.Entry(janela)
        entry_pago.pack()

        resultado_label = tk.Label(janela, text="", fg="blue")
        resultado_label.pack(pady=10)

        def finalizar_compra():
            nome = entry_nome.get().strip().lower()
            try:
                qtd = int(entry_qtd.get())
                pago = float(entry_pago.get())
                resposta = self.caixa.processar_compra(nome, qtd, pago)

                if resposta["sucesso"]:
                    resultado_label.config(
                        text=f"{resposta['mensagem']}\nTotal: R$ {resposta['total']:.2f}\nTroco: R$ {resposta['troco']:.2f}\nRestante: {resposta['restante']}",
                        fg="green"
                    )
                else:
                    resultado_label.config(text=resposta["mensagem"], fg="red")
            except ValueError:
                resultado_label.config(text="Insira valores válidos!", fg="red")

        tk.Button(janela, text="Finalizar Compra", command=finalizar_compra).pack(pady=5)

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_qtd.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def sair(self):
        self.db.fechar()
        self.root.destroy()
