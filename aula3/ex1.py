
saida = ""
for i in range(1, 101):
    print(i)
    saida = saida + " " + str(i) 
print(saida)

saida = ""
for i in range(100, 0, -1):
    print(i)
    saida = saida + " " + str(i)
print(saida)

for i in range(1, 101):
    print(100 - i+1)