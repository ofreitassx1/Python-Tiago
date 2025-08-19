lista = []

while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("O valor foi adicionado")
    else:
        print("O valor ja existe na lista")

    r = str(input("Quer continuar? [S/N]: "))
    if r in "Nn":
        break

print ("-="*25)
print(f"Voce digitou os valores: {lista}")
lista.sort()
print(f"Valores em ordem crescnte: {lista}")
lista.sort(reverse=True)
print(f"Valores em ordem decrescent: {lista}")
