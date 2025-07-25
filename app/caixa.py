from app.backend_mysql import Backend

class Caixa:
    def __init__(self):
        self.db = Backend()

    def processar_compra(self, nome_produto, quantidade_desejada, valor_pago):
        # Buscar produto no banco de dados
        resultado = self.db.buscar_produto(nome_produto)
        if not resultado:
            return {"sucesso": False, "mensagem": "❌ Produto não encontrado no estoque."}

        quantidade_estoque, preco_unitario = resultado

        # Verifica se há estoque suficiente
        if quantidade_desejada > quantidade_estoque:
            return {"sucesso": False, "mensagem": "⚠️ Quantidade maior do que o disponível em estoque."}

        # Calcula o total e verifica o pagamento
        total = quantidade_desejada * preco_unitario
        if valor_pago < total:
            return {
                "sucesso": False,
                "mensagem": f"⚠️ Valor insuficiente. Total: R$ {total:.2f}, pago: R$ {valor_pago:.2f}"
            }

        # Atualiza o estoque
        nova_qtd = quantidade_estoque - quantidade_desejada
        self.db.atualizar_quantidade(nome_produto, nova_qtd)
        troco = valor_pago - total

        return {
            "sucesso": True,
            "mensagem": f"✅ Compra de {quantidade_desejada}x '{nome_produto}' realizada com sucesso!",
            "total": total,
            "troco": troco,
            "restante": nova_qtd
        }
