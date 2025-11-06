# Escreva uma função que adicione um valor em um vetor
#  somente se ele não estiver presente.

import random

valores = []
tam = 10

for i in range(tam):
    valor = int(input(f"Entra com o valor {i+1}: "))
    valores.append(valor)

# valores = []
# for i in range(tam):
#     valores.append(random.randint(0, 100))

# valores = [random.randint(0, 100) for i in range(tam)]

encontrado = False
numero_novo = int(input("Entra com o valor para adicionar: "))

for i in range(tam):
    if valores[i] == numero_novo:
        encontrado = True

# for item in valores:
#     if item == numero_novo:
#         encontrado = True

if numero_novo not in valores:
    valores.append(numero_novo)
    print(valores)
else:
    print("Valor já existente")

if not encontrado:
    valores.append(numero_novo)
    print(valores)
else:
    print("Valor já existente")