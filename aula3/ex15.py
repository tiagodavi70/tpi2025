
soma = 0
maiorIdade = int("-inf")

i = 0
while i != 15:
    peso = float(input("Entra com o peso: "))
    idade = int(input("Entra com o idade: "))
    if idade >= 12:
        i += i
        soma += peso
        if maiorIdade < idade:
            maiorIdade = idade

print(maiorIdade, soma/15)