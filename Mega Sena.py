import time
from random import randint

lista = []
jogos = []
contador = []
print("-="*10, "Jogo da Mega Sena", "-="*10)

quantidade = int(input("Quantos jogos voce deseja jogar? \nR: "))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        
        if contador > 6:
            break
    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print("-="*8, f"Sorteando {quantidade} jogos", "-="*8)
print()
for i, n in enumerate(jogos):
    time.sleep(1)
    print(f'{i+1}º Jogo: {n}')

time.sleep(1)
print()
print("-="*8, "    Boa sorte    ", "-="*8)
