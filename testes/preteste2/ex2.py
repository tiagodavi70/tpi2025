# Escreva um script que preencha uma lista com os números de 50 até 100.
# Em seguida o utilizador pode entrar com um número indeterminado de números,
# retirando da lista os números que estão nessa lista.
# Ao fim da execução deve indicar a soma dos números restantes.


lista = []
for i in range(50, 101):
    lista.append(i)

lista = list(range(50, 101))

parar = ""
excluidos = []
while parar != "q":
    parar = input("Entra com um número('q' para parar): ")
    if parar != "q":
        numero = int(parar)
        excluidos.append(numero)

listaNova = []
for item in lista:
    if item not in excluidos:
        listaNova.append(item)

# 2º método
# for i in range(len(excluidos)):
#     if excluidos[i] in lista:
#         indice = lista.index(excluidos[i])
#         lista.pop(indice)

print(lista)
print(excluidos)
print(listaNova)