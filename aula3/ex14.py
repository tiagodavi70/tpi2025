
maiorMulher = float("-inf")
nomeMenorMulher = 0
maiorHomem = float("-inf")

menorHomem = float("inf")
menorMulher = float("inf")

somaMulher = 0
contMulher = 0

contadorHomem = 0

continuar = "s"
while continuar != "q":
    nome = input("Entra com o número: ")
    sexo = input("Entra com o sexo (m/f): ")
    altura = float(input("Entra com a altura: "))

    if sexo == "m":
        contadorHomem += 1
        if maiorHomem < altura:
            maiorHomem = altura    
        if menorHomem > altura:
            menorHomem = altura
    elif sexo == "m":
        contadorMulher += 1
        somaMulher += altura
        if maiorMulher < altura:
            maiorMulher = altura    
        if menorMulher > altura:
            menorMulher = altura
    
    
    continuar = input("Continuar (q - sair)?: ")

print(contadorHomem, menorHomem, maiorHomem)
print(nomeMenorMulher, (somaMulher/contadorMulher),menorMulher, maiorMulher)