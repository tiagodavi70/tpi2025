valor = input("Entra com um valor entre 0 e 60: ")
valor = int(valor)

sucessor = (valor + 1) % 61

print("Sucessor: " + str(sucessor))