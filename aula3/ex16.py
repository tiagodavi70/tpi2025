
quantidade50 = 0
soma1020 = 0
quantidadeMenor40 = 0

for i in range(12):
    idade = int(input("Entra com o idade: "))
    peso = float(input("Entra com o peso: "))
    altura = float(input("Entra com o altura: "))

    if idade > 50:
        quantidade50 += 1
    
    if (idade > 10) and (idade < 20):
        soma1020 += altura

    if peso < 40:
        quantidadeMenor40 += 1

print(quantidade50, soma1020/12, quantidadeMenor40/12)