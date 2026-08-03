n = int(input("escreva um numero inteiro:"))
soma =0
i= 0

while i < n:
    if i%2 == 0:
        soma+= i*i
    i+= 1

print(soma)