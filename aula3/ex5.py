# Escreva um script que mostre na tela a soma dos 200 primeiros ímpares.

contador = 0
soma = 0

for i in range(1, 400, 2):
    #print(i)
    soma = soma + i
    contador = contador + 1

print(contador, soma)


contadorImpar = 0
total = 1
soma = 0

while contadorImpar != 200:

    if total % 2 == 1:
        #print(acumulador)
        contadorImpar = contadorImpar + 1
        soma = soma + total
    
    total = total + 1
print(contadorImpar, soma)

soma = 0
contador = 0
for i in range(1, 99999999999999):
    if i % 2 == 1:
        soma = soma + i
        contador += 1
    
    if contador == 200:
        break

print(contador, soma)

total = 0
contador = 0
soma = 0
while True:
    total += 1
    if total % 2 == 1:
        soma = soma + total
        contador = contador + 1
    
    if contador == 200:
        break
    
print(contador, soma)

soma = 0
contador = 0
for i in range(1, 99999999):
    if i % 2 == 0:
        continue

    soma = soma + i
    contador = contador + 1

    if contador == 200:
        break

print(contador, soma)