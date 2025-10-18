angulo1 = float(input("introduza o pirmeiro angulo : "))
angulo2 = float(input("introduza o segundo angulo : "))
angulo3 = float(input("introduza o treceiro angulo : "))

soma = angulo1 + angulo2 + angulo3

if soma == 180 :
    print("Os angulos fazem um triangulo valido")
elif soma > 180 : 
    print(f"A soma dos angulos que é {soma} é maior que 180")
elif soma < 180 :
    print(f"A soma dos angulos que é {soma} é menor que 180")