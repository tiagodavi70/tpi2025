# 1. Escreva um script que faça o controle de carga de um depósito.
# O menu principal deve dar entrada de uma entrega por meio de um
# código. Cada entrega deve ficar em uma determinada área.
# O script deve permitir também dar saída de uma entrega.
# Deve salvar o histórico das entregas.

# Entrega - codigo, área, entregue (T, F)

def entregasNaoEntregue(entregas):
    for item in entregas:
        if not item["entregue"]:
            print(f"{item['codigo']} - {item['area']}")

opcao = 0
entregas = []
while opcao != 4:
    opcao = int(input('''1 - Entrada\n2 - Saida\n3 - Historico\n4 - Sair do programa\nEntra com a opção: '''))
    if opcao == 1:
        codigo = input("Entra com o código: ")
        area = input("Entra com a área: ")
        entregas.append({"codigo": codigo, "area": area, "entregue": False})
    elif opcao == 2:
        entregasNaoEntregue(entregas)
        codigoEntrega = input("Entra com o código: ")
        for item in entregas:
            if codigoEntrega == item["codigo"]:
                item["entregue"] = True
                print("Item entregue")
    elif opcao == 3:
        for item in entregas:
            print(f"{item['codigo']} - {item['area']} - {item['entregue']}")
    elif opcao == 4:
        print("Saindo...")