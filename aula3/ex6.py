
soma = 0
contador = 0
numero = 0

while numero >= 0:
    numero = float(input("Entra com o numero(número negativo para parar): "))
    if numero >= 0:
        soma += numero # soma = soma + numero
        contador += 1

print(soma/contador)