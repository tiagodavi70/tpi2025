numero = int(input("Entra com o numero: "))

divisao = numero // 2
resto = numero - (divisao * 2)

if resto == 0: # numero % 2 == 0
    print("Par")
else:
    print("Ímpar")