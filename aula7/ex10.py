import random

tam = 10
valores = []
for i in range(tam):
    valores.append(random.randint(50,100))

menor = float("inf")
maior = float("-inf")

for i in range(tam):
    if valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor:
        menor = valores[i]

valoresNormalizados = []
for i in range(tam):
    normalizado = (valores[i] - menor) / (maior - menor)
    valoresNormalizados.append(normalizado)

valores_string = []
for i in range(tam):
    valores_string.append(f"{valoresNormalizados[i]:.2f}")

print(valores)
print(valoresNormalizados)
print(valores_string)