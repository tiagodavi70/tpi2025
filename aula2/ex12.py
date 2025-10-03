'''
Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:

Compra 	Valor da Venda
menor que R$ 10 	Lucro de 70 %
entre R$ 10 e R$ 30 	Lucro de 50 %
entre R$ 30 e R$ 50 	Lucro de 40 %
maior que R$ 50 	Lucro de 30 %
Escreva um script que possa entrar com nome do produto e valor da
compra e imprimir o nome do produto e valor de venda.
'''
nomeProduto = input("Entra com o nome do produto: ")
valorCompra = float(input("Entra com o valor de compra: "))

lucro = 0

if valorCompra < 10:
    lucro = 70/100
elif (valorCompra >= 10) and (valorCompra < 30):
    lucro = 50/100
elif (valorCompra >= 30) and (valorCompra < 50):
    lucro = 40/100
elif valorCompra > 50:
    lucro = 30/100

valorVenda = valorCompra + (valorCompra * lucro)

print(f"{nomeProduto} : {valorVenda}")