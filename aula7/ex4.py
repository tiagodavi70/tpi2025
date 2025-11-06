import random

n = int(input("Entra com um valor"))

numeros = []
for i in range(n):
    numeros.append(random.randint(1,10))

print(numeros)