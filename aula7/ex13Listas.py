# Escreva um script quer faça o controle de estoque de uma loja. Em um menu deve ter as opções:
#     cadastrar produto
#     editar produto
#     vender pruduto
#     gerar relatório

# Na opção de cadastro o usuário deve entrar com:
#     nome do produto
#     preço
#     tipo

# Para cada produto cadastrado deve ser gerado um código.
# Na opção de editar deve permitir atualização do nome do produto.
# Na opção vender produto deve registrar uma venda do produto.
# E na opção gerar relatório deve mostrar o valor total ganho e a média por produto.

def listarProdutos(nomes, precos, tipos):
    for i in range(len(nomes)):
        print(f"{i} - {nomes[i]} | {tipos[i]} | {precos[i]}")

nome = []
preco = []
tipo = []

venda = []

opcao = 0
while opcao != 5:
    print("Entra com tua opção: \n1 - Cadastrar\n2 - Editar nome\n3 - Vender\n4 - Relatório\n5 - Finalizar")
    opcao = int(input())
    if opcao == 1:
        entradaNome = input("Entra com o nome: ")
        entradaTipo = input("Entra com o tipo: ")
        entradaPreco = float(input("Entra com o preco: "))
        nome.append(entradaNome)
        tipo.append(entradaTipo)
        preco.append(entradaPreco)
    elif opcao == 2:
        listarProdutos(nome, preco, tipo)
        indice = int(input("Entra com o codigo do produto para alterar o nome: "))
        novoNome = input("Entra com o novo nome: ")
        nome[indice] = novoNome
    elif opcao == 3:
        listarProdutos(nome, preco, tipo)
        indice = int(input("Entra com o codigo do produto para a venda: "))
        if indice >= 0 and indice < len(nome):
            venda.append(indice)
    elif opcao == 4:
        valorTotal = 0
        for i in range(len(venda)):
            valorTotal = valorTotal + preco[venda[i]]
        print(f"Valor total: {valorTotal}")

        tiposUnicos = []
        for i in range(len(tipo)):
            if tipo[i] not in tiposUnicos:
                tiposUnicos.append(tipo[i])
        
        for tipoUnico in tiposUnicos:
            soma = 0
            contador = 0
            for i in range(len(venda)):
                if tipoUnico == tipo[venda[i]]:
                    soma = soma + preco[venda[i]]
                    contador = contador + 1
            print(f"Média de {tipoUnico}: {soma/contador}")
            