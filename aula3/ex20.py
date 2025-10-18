numero = int(input("Entra com um número: "))
primo = True

if numero <= 1:
    primo = False
else:
    i = 2
    while i * i <= numero: # ou i/2 em algumas soluções, mas i*i é a solução ideal
        if numero % i == 0:
            primo = False
        i += 1

if primo:
    print(numero, "é primo.")
else:
    print(numero, "não é primo.")