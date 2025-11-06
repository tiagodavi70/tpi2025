vet = []
vet2 = [1, 2, 3, 4, 5]
vet3 = [0] * 5
vet4 = vet2 + vet3

print(vet, vet2, vet3)
print(vet2[1])
print("Tiago"[1])
print(vet4)
print("a" * 10)

vetorA = [0] * 5
print(len(vetorA))
for i in range(len(vetorA)):
    vetorA[i] = int(input("Entra com um número: "))

for i in range(len(vetorA)):
    print(str(i) + " " + str(vetorA[i]))
    print(f"{i} {vetorA[i]}")

print(vetorA)

vetorB = []
for i in range(10):
    vetorB.append(0)
print(vetorB)

soma = sum(vetorA)
minimo = min(vetorA)
maximo = max(vetorA)

