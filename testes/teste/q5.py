contadorVestuario = 0
contadorCalcado = 0
escolha = ""
somaPrecoVestuario = 0
somaPrecoCalcado = 0

while escolha == "q":

    tipo = input("Vestuario ou calçado?")
    preco = float(input("Entra com o preço: "))

    if tipo == "vestuario":
        contadorVestuario += 1
        somaPrecoVestuario = somaPrecoVestuario + preco
    elif tipo == "calçado":
        contadorCalcado += 1
        somaPrecoCalcado = somaPrecoCalcado + preco

    escolha = input("Quer continuar? (q - sair) :")

descontoVestuario = (contadorVestuario // 5) * (2/100) * somaPrecoVestuario
precoFinalVestuario = somaPrecoVestuario - descontoVestuario
descontoCalcado = (contadorCalcado // 2) * (1/100) * somaPrecoCalcado
preçoFinalCalcado = somaPrecoCalcado - descontoCalcado

precoFinalTotal = precoFinalVestuario + preçoFinalCalcado 

print(f"O preço final a pagar é {precoFinalVestuario} euros pelo vestuario e {preçoFinalCalcado} euros pelo calçado que da um total de {precoFinalTotal} euros.")