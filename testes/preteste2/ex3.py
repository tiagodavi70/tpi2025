# Dadas duas listas de 100 posições cada, encontre todos os pares na
# mesma posição em que os elementos do primeiro vetor são menores que
# os elementos do segundo vetor.

import random

lista1 = []
lista2 = []
for i in range(100):
    lista1.append(random.randint(1,1000))
    lista2.append(random.randint(1, 1000))

for i in range(100):
    v1 = lista1[i]
    v2 = lista2[i]
    if v1 < v2:
        print(f"{v1} < {v2}")