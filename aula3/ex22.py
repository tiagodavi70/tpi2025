totalGraos = 0
graosNaCasa = 1
casa = 1

while casa <= 64:
    totalGraos += graosNaCasa
    graosNaCasa = graosNaCasa * 2
    casa += 1

print(totalGraos)