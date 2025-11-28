# 2. Escreva um script que receba informação sobre colaboradores
# de uma fábrica. Para o cadastro, deve receber idade, salário,
# cargo e freguesia onde vive. Deve permitir busca por nome,
# e filtra salário por um limite maior e menor. Deve permitir
# editar salário, cargo e freguesia. 

opcao = 0
colaboradores = []
while opcao == 5:
    opcao = int(input("1 - Cadastro\n2 - Buscar Nome\n3 - Filtrar por salário\n4 - Editar\n5 - Sair"))
    if opcao == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        salario = float(input("Salário: "))
        cargo = input("Cargo: ")
        freguesia = input("Freguesia: ")
        colaboradores.append({"nome": nome, "idade": idade,
                              "salario": salario, "cargo": cargo,
                              "freguesia": freguesia})
    elif opcao == 2:
        nomeBusca = input("Entra com o nome: ")
        for colaborador in colaboradores:
            if nomeBusca == colaborador["nome"]:
                print(f"{colaborador['nome']} - {colaborador['idade']} - {colaborador['cargo']}")
    elif opcao == 3:
        escolhaTipo = int(input("Selecione o tipo: 1 - buscar maior 2 - buscar menor"))
        salarioFiltro = float(input("Entra com o valor do salário: "))
        if escolhaTipo == 1:
            for colaborador in colaboradores:
                if colaborador["salario"] > salarioFiltro:
                    print(f"{colaborador['nome']} - {colaborador['salario']} - {colaborador['cargo']}")
        else:
            for colaborador in colaboradores:
                if colaborador["salario"] < salarioFiltro:
                    print(f"{colaborador['nome']} - {colaborador['salario']} - {colaborador['cargo']}")
    elif opcao == 4:
        for (i, colaborador) in enumerate(colaboradores):
            print(f"{i+1} - {colaborador['nome']} - {colaborador['salario']} - {colaborador['cargo']}")
        codigo = int(input("Entra com o codigo: ")) - 1
        opcaoEdicao = int(input("1 - salario | 2 - cargo | 3 - freguesia"))
        if opcaoEdicao == 1:
            colaboradores[codigo]["salario"] = float(input("Entra com o salário novo: "))
        elif opcaoEdicao == 2:
            colaboradores[codigo]["cargo"] = input("Entra com o novo cargo: ")
        elif opcaoEdicao == 3:
            colaboradores[codigo]["freguesia"] = input("Entra com a nova freguesia: ")
        else:
            print("Opcao inválida")
    elif opcao == 5:
        print("Saindo..")
