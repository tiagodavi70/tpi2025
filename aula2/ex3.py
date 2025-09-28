nota = float(input("Entra com a nota: "))

if (nota >= 0) and (nota < 5):
    print("Insuficiente")
elif (nota >= 5) and (nota < 7):
    print("Regular")
elif (nota >= 7) and (nota < 9):
    print("Bom")
elif (nota >= 9) and (nota <= 10):
    print("Excelente")
else:
    print("Nota inválida")