import random

# Multiplicação pontual

#vetor = list(range(2, 100, 2))

lista1 = []
lista2 = []
for i in range(10):
    lista1.append(random.randint(1,10))
    lista2.append(random.randint(1,10))

if len(lista1) == len(lista2):
    multiplicaoPontual = []
    for i in range(len(lista1)):
        valorMultiplicacao = lista1[i] * lista2[i]
        multiplicaoPontual.append(valorMultiplicacao)
print(lista1)
print(lista2)
print(multiplicaoPontual)

# Multiplicacao
multiplicao = 0
for i in range(len(lista1)):
    valorMultiplicacao = lista1[i] * lista2[i]
    multiplicao = multiplicao + valorMultiplicacao
print(multiplicao)