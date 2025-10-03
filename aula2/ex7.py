
mes = int(input("Entra com um numero entre 1 e 12:"))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
else:
    print("Número inválido")

if (mes > 0) and (mes <= 12):
    if mes == 1:
        print("Janeiro")
    else:
        if mes == 2:
            print("Fevereiro")
        else:
            if mes == 3:
                print("Março")
else:
    print("Número inválido")

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case _:
        print("Número inválido")