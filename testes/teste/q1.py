nome1 = input("Introduza o nome da primeira pessoa :")
idade1 = int(input("Introduza a idade da primeira pessoa :"))
nome2 = input("Introduza o nome da segunda pessoa :")
idade2 = int(input("Introduza a idade da segunda pessoa :"))

if idade1 < idade2 :
    print(f"O/A {nome2} que tem {idade2} anos é mais velho/a que o/a {nome1}")
elif idade2 < idade1 :
    print(f"O/A {nome1} que tem {idade1} anos é mais velho/a que o/a {nome2}")
