class Caixa:
    def __init__(self, nome):
        self.nome = nome

    def processar_pagamento(self, metodo, valor):
        print(f"{self.nome} vai processar o pagamento...")
        metodo.pagar(valor)

# Classes de formas de pagamento
class CartaoCredito:
    def pagar(self, valor):  # ✅ Corrigido: self em vez de --
        print(f" Pagando R${valor:.2f} com cartão de crédito.")

class Dinheiro:
    def pagar(self, valor):  # ✅ Corrigido
        print(f" Pagando R${valor:.2f} em dinheiro.")

class Pix:
    def pagar(self, valor):  # ✅ Corrigido
        print(f" Pagando R${valor:.2f} via Pix.")

# Criando objetos CORRETAMENTE
caixa = Caixa("Caixa do Supermercado")

cartao = CartaoCredito()  # ✅ Sem parâmetros
dinheiro = Dinheiro()     # ✅ Sem parâmetros  
pix = Pix()               # ✅ Sem parâmetros

class Cupom:
    def imprimir(self):
        print("Cupom de desconto de R$10,00.")

cupom = Cupom()

# Exemplo de uso correto:
caixa.processar_pagamento(cartao, 150.50)
caixa.processar_pagamento(dinheiro, 75.25)
caixa.processar_pagamento(pix, 200.00)
cupom.imprimir()