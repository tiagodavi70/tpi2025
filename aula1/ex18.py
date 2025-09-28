
valor = float(input("Entra com o valor: "))

contagem = valor // 100

desconto = contagem * (0.05/100) # 0.05% | 0.0005

formatado = valor - desconto
#formatado = "{:.2f}".format(formatado)

print("Valor com desconto: " + str(formatado))