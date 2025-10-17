"""
A loja OAZ Sports apresenta um conjunto de descontos que depende do tipo e a quantidade
de itens comprados. Para cada 4 peças do tipo vestuário o cliente ganha 2% de desconto, e
para cada 2 peças de calçados ganha 3% de desconto. Escreva um script que simule um
caixa, que leia um produto de cada vez com seu preço e tipo, e no final aplique o desconto
sobre a compra total.
"""

contadorVestuario = 0
contadorCalcados = 0

totalVestuario = 0
totalCalcados = 0

preco = 0
tipo = ""

while tipo != "q":
    tipo = input("Entra com o tipo (vestuario/calcado): ")
    if tipo != "q":
        preco = float(input("Entra com o preço: "))
        if tipo == "vestuario":
            contadorVestuario = contadorVestuario + 1
            totalVestuario = totalVestuario + preco
        elif tipo == "calcado":
            contadorCalcados = contadorCalcados + 1
            totalCalcados += preco # totalCalcados = totalCalcados + preco
        else:
            print("tipo inválido")

descontoVestuario = (2/100) * (contadorVestuario // 4)
descontoCalcado = (3/100) * (contadorCalcados // 2)

totalSemDesconto = totalVestuario + totalCalcados
desconto = (descontoVestuario + descontoCalcado) * totalSemDesconto

total = totalSemDesconto - desconto

print(descontoVestuario, descontoCalcado, totalSemDesconto, desconto)
print("Valor total de compra: " + str(total))
