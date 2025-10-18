numero1 = float(input("Introduza o primeiro numero : "))
numero2 = float(input("Introduza o segundo numero : "))

if numero1 < numero2 :
    diferença = numero2 - numero1
    print(f"A diferença do {numero2} pelo {numero1} é {diferença}")
elif numero2 < numero1 :
    diferença = numero1 - numero2
    print(f"A diferença do {numero1} pelo {numero2} é {diferença}")
else :
    print("Os numeros são iguais")