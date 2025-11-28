# Escreva um script que crie uma lista de 600 lançamentos aleatórios de dados.
# Indique ao final qual a quantidade de vezes que cada número apareceu.

import random 

lista = []

for i in range(600):
    lancamentoDado = random.randint(1, 6)
    lista.append(lancamentoDado)

# 1º método
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
contador6 = 0

for dado in lista:
    if dado == 1:
        contador1 = contador1 + 1
    elif dado == 2:
        contador2 = contador2 + 1
    elif dado == 3:
        contador3 = contador3 + 1
    elif dado == 4:
        contador4 = contador4 + 1
    elif dado == 5:
        contador5 = contador5 + 1
    elif dado == 6:
        contador6 = contador6 + 1

print(f"{contador1} - {contador2} - {contador3} - {contador4} - {contador5} - {contador6}")

# 2º método
contador = [0] * 6
for dado in lista:
    contador[dado - 1] += 1 # contador[dado - 1] = contador[dado - 1] + 1 

print(contador)