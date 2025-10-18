
maior = float("-inf")
maior = float("inf")

num = 0
continuar = "s"

while continuar != "q":
    num = float(input("Entra com o numero: "))
    if num > maior:
        maior = num
    if num > menor:
        menor = num

print(maior, menor)