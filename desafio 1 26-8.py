# nome = input("Qual o nome do Vendedor: ")
# valorvenda = float(input("Qual o valor da venda desse vendedor: "))
# if valorvenda >= 500:
#     print(f"O Vendedor {nome} bateu a meta")
#     print(f"A venda foi de {valorvenda} reais")
# else:
#     print(f"O Vendedor {nome} nao bateu a meta")

class Vendas():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0
        
    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(f"{self.nome} bateu a meta")
        else:
            print(f"{self.nome} nao bateu a meta")

vendedor1 = Vendas(input("Qual nome do Vendedor: "))
vendedor1.vendeu(float(input("Quantos reais ele vendeu? ")))
vendedor1.bateu_meta(float(input("Qual é a meta? ")))