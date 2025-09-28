# Venda de bilhetes para um museu
# +60 anos
# -6 anos
# somente domingos

idade = int(input("Entra com tua idade: "))
dia = input("Entra com o dia da semana: ")

if ((idade >= 60) or (idade <= 6)) and (dia == "domingo"):
    print("Bilhete gratuito")
else:
    print("Pague o bilhete")

# if idade < 60:
#     print("Pague o bilhete")

print("Volte sempre")