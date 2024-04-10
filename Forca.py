# criando a coleção de palavras
palavras = ["brasil", "uruguai", "inglaterra", "australia"]

# pedindo a adição de no mínimo mais 3 palavras com mais de 4 letras
i = 1
while True:
    palavrinha = input('Digite uma palavra ou "s" para terminar: ').lower()
    if palavrinha == 's' and i > 3:
        break
    elif len(palavrinha) < 5:
        print(f'{palavrinha} não vale. Tem que ter mais de 4 letras.')
    else:
        palavras.append(palavrinha)
        i += 1
print(palavras)

# escolhendo uma palavra
from random import randint
palavra = palavras[randint(0, len(palavras) - 1)]
print(palavra)

# montando a mascara da palavra
tentativa = []
mascara = ""
i = 0
while i < len(palavra):
    tentativa.append("_ ")
    i += 1

forca = 0
acertos = 0
letrasTentadas = []
while True:
    # desenhando a forca
    print("\n" * 10)
    print("##### JOGO DA FORCA #####")
    print("=" * 25)
    print("\n |¨¨¨¨¨", end='')
    if forca > 0: print("|", end='')
    print("\n |", end='')
    if forca > 1: print("     O", end='')
    print("\n |", end = '')
    if forca > 2: print("    /", end='')
    if forca > 3: print("|", end='')
    if forca > 4: print("\\", end='')
    print("\n |", end='')
    if forca > 5: print("     |", end='')
    print("\n |", end = '')
    if forca > 6: print("    /", end='')
    if forca > 7: print(" \\", end='')
    print("\n_|__      ", end='')
    for c in tentativa:
        print(c, end=' ')
    print(f"\nPalavra com {len(palavra)} letras.")
    print("=" * 25)

    # verifica vitória ou forca
    if acertos == len(palavra):
        print("####  Você venceu!  ####")
        exit()
    elif forca == 8:
        print("##  Você foi enforcado!  ##")
        exit()

    # jogada
    while True:
        letraEscolhida = input("Escolha uma letra: ")
        if letraEscolhida in letrasTentadas:
            print(f'Não vale. A letra "{letraEscolhida}" já foi tentada')
        else:
            letrasTentadas.append(letraEscolhida)
            break
    encontreiUmaLetra = False
    for indice, letra in enumerate(palavra):
        if letra == letraEscolhida:
            tentativa[indice] = letra
            acertos += 1
            encontreiUmaLetra = True
    if encontreiUmaLetra == False:
            forca += 1


