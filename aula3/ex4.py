
num1 = int(input("Entra com o número 1: "))
num2 = int(input("Entra com o número 2: "))

# 2 6 = 2 + 3 + 4 + 5 + 6

soma = 0
for i in range(num1, num2 + 1):
    soma = soma + i

print(soma)