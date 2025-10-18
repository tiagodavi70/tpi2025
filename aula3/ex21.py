n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

if n == 0:
    fatorial = 1
else:
    i = 1
    while i <= n:
        fatorial = fatorial * i
        i += 1

print("O fatorial de", n, "é", fatorial)