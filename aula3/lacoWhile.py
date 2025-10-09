
i = 0
while i < 10:
    print(i)
    i = i + 1       # i += 1


j = 0
while j < 10:
    print(j)
    j += 1

idade = 1
contador = 0
contadorTotal = 0
while idade != 0:
    idade = int(input("Entra com a idade: "))
    if idade > 30:
        contador = contador + 1
    elif idade >= 0:
        contadorTotal += 1
    #contadorTotal += 1
#contadorTotal -= 1

print("Idades maiores que 30: " + str(contador))
print("Total: " + str(contadorTotal))