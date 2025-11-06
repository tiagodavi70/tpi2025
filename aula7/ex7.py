import random 

# Escreva um script que dado dois vetores indique os elementos que
# estão presentes nos dois vetores.

tamanho = 10

vet1 = []
vet2 = []
for i in range(tamanho):
    vet1.append(int(input("Entra com um número pro vetor 1: ")))
for i in range(tamanho):
    vet1.append(int(input("Entra com um número pro vetor 2: ")))

# alternativamente

vet1 = []
vet2 = []

continua = True
while continua:
    numero = input("Entra com um número pro vetor 1 (q para sair): ")
    if numero != "q":
        vet1.append(int(numero))
    else:
        continua = False

continua = True
while continua:
    numero = input("Entra com um número pro vetor 2 (q para sair): ")
    if numero != "q":
        vet2.append(int(numero))
    else:
        continua = False

# alternativamente
vet1 = []
vet2 = []
for i in range(tamanho * 10):
    vet1.append(random.randint(0,1000000))
    vet2.append(random.randint(0,1000000))

for i in range(len(vet1)):
    if vet1[i] in vet2:
        print(f"{vet1[i]} está nos dois vetores") 

for i in range(len(vet1)):
    for j in range(len(vet2)):
        if vet1[i] == vet2[j]:
            print(f"{vet1[i]} está nos dois vetores")