# Escreva um script que receba cinco números e
# diga a quantidade de números negativos.

num1 = float(input("Entra com o número: "))
num2 = float(input("Entra com o número: "))
num3 = float(input("Entra com o número: "))
num4 = float(input("Entra com o número: "))
num5 = float(input("Entra com o número: "))

contador = 0

if num1 < 0:
    contador = contador + 1
if num2 < 0:
    contador = contador + 1
if num3 < 0:
    contador = contador + 1
if num4 < 0:
    contador = contador + 1
if num5 < 0:
    contador = contador + 1

print("Quantidade de negativos: " + str(contador))