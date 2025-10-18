a = 0
b = 1

for i in range(1000):
    soma = a + b
    a = b
    b = soma

print(soma)