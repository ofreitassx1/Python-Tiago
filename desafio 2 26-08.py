# nome = input("Digite o seu nome: ")
# idade = int(input("Digite a sua idade: "))
# print(f"Ola, meu nome é {nome} e eu tenho {idade} anos")

class Apresentador():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir(self):
        print(f"Ola, meu nome é {self.nome} e eu tenho {self.idade} anos")
    
nome = input("Digite o seu Nome: ")
idade = (int(input("Digite a sua Idade: ")))
pessoa1 = Apresentador(nome, idade)
pessoa1.exibir()