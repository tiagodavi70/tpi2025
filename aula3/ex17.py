

totalL = 0
totalA = 0
totalH = 0

continuar = ""
while continuar != "q":
    codigo = input("Entra com o codigo: ")
    valor = float(input("Entra com o valor: "))

    if   codigo == "L":
        totalL += valor
    elif codigo == "H":
        totalH += valor
    elif codigo == "A":
        totalA += valor

    continuar = input("Continuar (q - sair)?: ")

print(totalA, totalH, totalL, totalA + totalH + totalL)