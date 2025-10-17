
numero = 0
contador = 0

while numero != -1:
    numero = float(input("Entra com um numero: "))
    if (numero > 50) and (numero < 150):
        contador = contador + 1

print("50 < n < 150: " + str(contador))