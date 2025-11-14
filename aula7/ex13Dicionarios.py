
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

def listarProdutos(prods):
    for i in range(len(prods)):
        print(f'{i} - {prods[i]["nome"]} | {prods[i]["tipo"]} | {prods[i]["preco"]}')        

produtos = []
vendas = []

opcao = 0
while opcao != 5:
    opcao = int(input("1 2 3 4 5 "))
    if opcao == 1:
        nome = input("Nome: ")
        tipo = input("Tipo: ")
        preco = float(input("Preço: "))
        produto = {"nome": nome, "tipo": tipo, "preco": preco}
        produtos.append(produto)
    elif opcao == 2:
        listarProdutos(produtos)
        indice = int(input("Indice"))
        novoNome = input("Nome")
        produto[indice]["nome"] = novoNome
    elif opcao == 3:
        listarProdutos(produtos)
        indice = int(input("Indice"))
        if indice >= 0 and indice < len(produtos):
            vendas.append(indice)
    elif opcao == 4:
        valorTotal = 0
        for i in range(len(vendas)):
            valorTotal = valorTotal + produtos[vendas[i]]["preco"]
        print(valorTotal)

        tiposUnicos = []
        for prod in produtos:
            if prod["tipo"] not in tiposUnicos:
                tiposUnicos.append(prod["tipo"])
        
        for tipo in tiposUnicos:
            soma = 0
            contador = 0
            for prod in produtos:
                if prod["tipo"] == tipo:
                    soma += prod["preco"]
                    cont += 1
            print(f'Média de {tipo}: {soma/contador}')
        