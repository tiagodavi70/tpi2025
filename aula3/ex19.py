
contadorC = 0 
contadorS = 0
contadorD = 0
contadorV = 0
total = 0

somaV = 0
somaD = 0

continuar = ""
while continuar != "q":
    estadoCivil = input("Entra com o estado civil: ")
    idade = int(input("Entra com a idade: "))

    total += 1

    if estadoCivil == "C":
        contadorC += 1
    elif estadoCivil == "S":
        contadorS += 1
    if estadoCivil == "V":
        somaV += V
        contadorV += 1
    elif estadoCivil == "D":
        contadorD += 1

    continuar = input("Continuar? (q - para sair): ")

print(contadorC, contadorS, somaV / contadorV, contadorD / total )