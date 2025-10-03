a = float(input("Entra com o numero 1: "))
b = float(input("Entra com o numero 2: "))
c = float(input("Entra com o numero 3: "))

if a > b:
    if a > c:
        if b > c:
            print(a, b, c)
        else:
            print(a, c, b)
    else:
        print(c, a, b)
else:
    if a > c:
        print(b, a ,c)
    elif c > b:
        print(c, b, a)
    else:
        print(b, c, a)