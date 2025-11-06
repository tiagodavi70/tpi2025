

tamanho = 5
nomes = []
for i in range(tamanho):
    nomes.append(input("Entra com o nome: "))

nomeBusca = input("Entra com o nome pra buscar: ")
encontrado = False
for nome in nomes:
    if nome == nomeBusca:
        encontrado = True

if encontrado:
    print("Nome encontrado")
else:
    print("Nome não encontrado")

if nomeBusca in nomes:
    print("Nome encontrado")
else:
    print("Nome não encontrado")