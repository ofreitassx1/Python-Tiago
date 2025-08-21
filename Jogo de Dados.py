from random import randint
from time import sleep
dados = []
jogadores = {
    "Jogador 1" : randint(1, 6),
    "Jogador 2" : randint(1, 6),
    "Jogador 3" : randint(1, 6),
    "Jogador 4" : randint(1, 6)
}
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "Valores Sorteados" "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
for keys, values in jogadores.items():
    print(f"{keys} tirou {values} no dado")
    sleep(1)
print("-="*20)

for i, values in enumerate(dados):
    print(f"{i+1}° {values[0]} com {values[1]} pontos")