lista = []
listapar = []
listaimpar = []

while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        if n % 2 == 0:
            listapar.append(n)
            print ("O numero foi adicionado na lista")
        else:
            listaimpar.append(n)
            print ("O numero foi adicionado a lista")
    else:
        print ("O numero ja existe")
          
    r = str(input("Deseja continuar adicionando? [S/N]"))
    if r in "Nn":
        break

print ("-="*25)
print (f"Os numeros adicionados na lista foram: {lista}")
print (f"Os numeros pares adicionados sao: {listapar}")
print (f"Os numeros impares adicionados sao: {listaimpar}")

