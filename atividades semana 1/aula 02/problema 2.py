lista = []
continuar = True

while continuar == True:
    novoItem = int(input("digite um numero:"))
    lista.append(novoItem)

    decisao = input("digitar outro numero?[s][n]")

    if decisao == 'n':
        continuar = False


def funcao(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j and lista[i] == lista[j]:
                return "Existem números iguais nessa lista"

    return "Todos os itens dessa lista são diferentes"

print(funcao(lista))