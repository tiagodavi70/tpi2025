nome = input("Entra com teu nome: ")
ano = input("Entra com teu ano de nascimento: ")
ano = int(ano)
anoAtual = input("Entra com o ano atual: ")
anoAtual = int(anoAtual)
idade = anoAtual - ano

print(nome + " sua idade é: " + str(idade))