# Escreva um script que receba um número
# e verifique se é divísivel por 6.

numero = int(input("Entra com o número: "))

if (numero % 6) == 0:
    print(str(numero) + " é divisível por 6.")
else:
    print(str(numero) + " não é divisível por 6.")

