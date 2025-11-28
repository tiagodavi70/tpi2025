
tamanho = 5
colaboradores = []
for i in range(tamanho):
    nome = input("Nome: ")
    salario = float(input("Salário: "))
    tempo = int(input("Tempo (meses): "))
    colaboradores.append({"nome": nome, "salario": salario, "tempo": tempo})

#maior e menor
# max(colaboradores, lambda x: x["salario"])

maior = float("-inf") # colaboradores[0]["salario"] 
menor = float("inf") # colaboradores[0]["salario"]

indiceMaior = -1 # 0
indiceMenor = -1 # 0

somaSalarios = 0

for i in range(len(colaboradores)):
    if maior < colaboradores[i]["salario"]:
        maior = colaboradores[i]["salario"]
        indiceMaior = i
    
    if menor > colaboradores[i]["salario"]:
        menor = colaboradores[i]["salario"]
        indiceMenor = i
    
    somaSalarios = somaSalarios + colaboradores[i]["salario"]

mediaSalarios = somaSalarios / tamanho
print(f"{colaboradores[indiceMaior]['nome']} {colaboradores[indiceMenor]['nome']} {mediaSalarios}")

contadorMaior = 0
contadorMenor = 0

for colaborador in colaboradores:
    if colaborador["salario"] > mediaSalarios:
        contadorMaior += 1
    if colaborador["salario"] < mediaSalarios:
        contadorMenor += 1

print(f"{contadorMaior} {contadorMenor}")