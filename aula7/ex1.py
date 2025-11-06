#Escreva um script que receba dez nomes do usuário,
# armazene-os em uma lista e ao final mostre a listagem,
# indicando a ordem de entrada de cada nome.

tamanho = 10
nomes = [""] * tamanho # [""] + [""] + [""] + [""] + [""] + [""] + [""] 
for i in range(tamanho):
    nomes[i] = input("Entra com o nome: ")

print(nomes)

# nomes = []
# for i in range(tamanho):
#     nomes.append(input("Entra com o nome: "))

for i in range(tamanho):
    print(f"{i+1} - {nomes[i]}")