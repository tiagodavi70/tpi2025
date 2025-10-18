print("=== Jogo do Marciano e do Caçador ===")
arvoreMarciano = int(input("Jogador 1, escolha uma árvore (1 a 100): "))

tentativas = 5
acertou = False
contador = 1

while contador <= tentativas:
    tiro = int(input("Tentativa " + str(contador) + " — escolha uma árvore entre 1 e 100: "))
    
    if tiro == arvoreMarciano:
        print("Você acertou o marciano!")
        acertou = True
        break
    elif tiro < arvoreMarciano:
        print("O marciano diz: estou mais à direita.")
    else:
        print("O marciano diz: estou mais à esquerda.")
    contador += 1

if not acertou:
    print("O caçador errou todas as tentativas! O marciano levou o caçador para Marte!")