lista = []
continuar = True

while continuar == True:
    novoItem = int(input("digite um numero:"))
    lista.append(novoItem)

    decisao = input("digitar outro numero?[s][n]")

    if decisao == 'n':
        continuar = False

def funcao(lista=[]):

    maior = lista[0]
    menor = lista[0]

    for item in lista:
        if(item<menor):
            menor = item
        if(item>maior):
            maior = item

    return (menor,maior)        


print(funcao(lista))
