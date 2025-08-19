lista = []
maior = 0 
menor = 0

for i in range(0, 5):                                                              # range de 0 a 5 para o usuario adicionar apenas 5 numeros
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))      # aqui é para o usuario adicionar o numero dentro da lista e o i é para saber a ordem que esta sendo adicionado 
    if i == 0: 
        maior = menor = lista[i]
    else:
        if lista[i] > maior:                                          # se o numero adicionado for maior que 0, a variavel "maior" vai virar o maior numero adicionado
            maior = lista[i]
        if lista[i] < menor:                                          # quando o maior numero adicionado na lista for adicionado, a variavel vai ser o menor numero
            menor = lista[i]

print (f'Os valores digitados foram: {lista}')                             # aqui é para aparecer no terminal os numeros que o usuario adicionou
print(f"O maior numero encontrador foi {maior} na posicao: ", end="")      # aqui é para mostrar que o maior numero foi X na posicao Y
for ind, num in enumerate(lista):                    # o ind mostra a posicao e o num mostra qual o numero
    if num == maior:                                 # se o numero for igual o maior, ele vai aparecer no terminal a sua posical
        print (f'{ind}', end="")                          # aqui vai aparecer no terminal a posicao e o end nao vai deixar quebrar a linha
print ()               # pra quebrar a linha

print(f"O menor numero encontrador foi {menor} na posicao: ", end="")      # aqui é para mostrar que o menor numero foi X na posicao Y
for ind, num in enumerate(lista):                           
    if num == menor:                         # se o numero for igual o menor, ele vai aparecer no terminal a sua posical                     
        print (f'{ind}', end="")                        # aqui vai aparecer no terminal a posicao e o end nao vai deixar quebrar a linha                             

print()               # pra quebrar a linha
print ("-="*25)
print ('-=-=-=-=-=-=-=-= Fim da lista -=-=-=-=-=-=-=-=-=-=')