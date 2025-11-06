numeros = []

continua = True
while continua:
    numero = input("Entra com um número (q para sair): ")
    if numero != "q":
        numeros.append(int(numero))
    else:
        continua = False

somatorio = sum(numeros)
media = somatorio / len(numeros)
print(somatorio, media)