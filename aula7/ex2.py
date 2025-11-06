# Escreva um script que crie um vetor com 10
# posições e receba seus valores do usuário.
# Ao final deverá mostrar somente os valores acima
# da média.

tamanho = 10
valores = [0] * tamanho
for i in range(tamanho):
    valores[i] = float(input("Entra com o valor: "))

media = sum(valores) / len(valores)

soma = 0
# for i in range(len(valores)):
#     soma += valores[i]

for item in valores:
    soma += item

print(media)
for item in valores:
    if item >= media:
        print(item)

# maiores = filter(lambda x : x >= media, valores)
# print(list(maiores))