

for i in range(10):
    print(f"{i}")

for i in range(5, 11):
    print(f"{i}")

for i in range(10, 101, 10):
    print(f"{i}")


for j in range(10, 5, -1):
    print(j)

contador = 0
for i in range(5):
    idade = int(input("Entra com a tua idade: "))
    print(idade)
    if idade > 30:
        contador = contador + 1

print("Idades maiores que 30: " + str(contador))
