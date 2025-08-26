saldo = 0
class Depositar():
    def __init__(self, valor):
        self.valor = valor

    def depositar(self, valor):
        print(f"O valor disponivel na conta é de {valor} reais")

pessoa1 = Depositar(input("Qual a conta que voce deseja depositar? "))
pessoa1.depositar(int(input("Digite a quantidade de Reais que voce quer depositar: ")))