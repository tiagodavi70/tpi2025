ouvintes_segunda = 2562
ouvintes_terça = 1237
ouvintes_quarta = 983
ouvintes_quinta = 1757
ouvintes_sexta = 3651
ouvintes_sabado = 5263
ouvintes_domingo = 4285
ouvintes_maior = -9999999999
ouvintes_menor = 9999999999

if ouvintes_segunda > ouvintes_maior :
    ouvintes_maior = ouvintes_segunda
if ouvintes_terça > ouvintes_maior : 
    ouvintes_maior = ouvintes_terça
if ouvintes_quarta > ouvintes_maior : 
    ouvintes_maior = ouvintes_quarta
if ouvintes_quinta > ouvintes_maior : 
    ouvintes_maior = ouvintes_quinta
if ouvintes_sexta > ouvintes_maior : 
    ouvintes_maior = ouvintes_sexta
if ouvintes_sabado > ouvintes_maior : 
    ouvintes_maior = ouvintes_sabado
if ouvintes_domingo > ouvintes_maior : 
    ouvintes_maior = ouvintes_domingo

if ouvintes_segunda < ouvintes_menor :
    ouvintes_menor = ouvintes_segunda
if ouvintes_terça < ouvintes_menor : 
    ouvintes_menor = ouvintes_terça
if ouvintes_quarta < ouvintes_menor : 
    ouvintes_menor = ouvintes_quarta
if ouvintes_quinta < ouvintes_menor : 
    ouvintes_menor = ouvintes_quinta
if ouvintes_sexta < ouvintes_menor : 
    ouvintes_menor = ouvintes_sexta
if ouvintes_sabado < ouvintes_menor : 
    ouvintes_menor = ouvintes_sabado
if ouvintes_domingo < ouvintes_menor : 
    ouvintes_menor = ouvintes_domingo

print(f"O dia com maior ouvintes foi {ouvintes_maior} que é Sabado")
print(f"O dia com menor ouvintes foi {ouvintes_menor} que é Quarta")