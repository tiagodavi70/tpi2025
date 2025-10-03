# Escreva um script que, para uma conta bancária,
# leio o seu número, o saldo, o tipo de operação a ser
# realizada (depósito ou retirada) e o valor da operação.
# Após, determine e mostre o novo saldo.

numeroConta = input("Entra com o número da conta: ")
saldo = float(input("Entra com o saldo da conta: "))
tipoOperacao = input("Entra com o tipo de operacao \nD - Deposito\nL - Levantamento: ")
valorOperacao = float(input("Entra com o valor da operacao: "))

if tipoOperacao == "D":
    saldo = saldo + valorOperacao # saldo += valorOperacao
elif tipoOperacao == "L":
    if saldo - valorOperacao >= 0:
        saldo = saldo - valorOperacao
    else:
        print("Não é possível realizar essa operação, não tem valor em conta o suficiente.")

print("Saldo: " + str(saldo))
print("Saldo: ", saldo)
