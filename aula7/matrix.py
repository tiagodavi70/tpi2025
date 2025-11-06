matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)

print(matrix[1][1])
print(matrix[2][0])
print(matrix[0][2])

tamLinhas = 5
tamColunas = 4

matrix2 = [[0] * tamColunas for _ in range(tamLinhas)]
print(matrix2)

matrix3 = []
for i in range(tamLinhas):
    matrix3.append([])
    for j in range(tamColunas):
        matrix3[i].append(0)

print(matrix3)