cidade = input("Entra com a cidade: ")

# cidades = Oliveira de Azeméis, Porto, Aveiro

if cidade == "Oliveira de Azeméis":
    print("OAZ")

if cidade == "Porto":
    print("POR")

if cidade == "Aveiro":
    print("AVE")

if cidade == "Oliveira de Azeméis":
    print("OAZ")
elif cidade == "Porto":
    print("POR")
elif cidade == "Aveiro":
    print("AVE")
else:
    print("Cidade não cadastrada")

if cidade:
    print("")
else:
    if (cidade):
        print("")

match cidade:
    case "Oliveira de Azeméis":
        print("OAZ")
    case "Porto":
        print("POR")
    case "Aveiro":
        print("AVE")