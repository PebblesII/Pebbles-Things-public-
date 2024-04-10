#UI
#Cria a lista com grades vaizias
casas = []
jogador = "O"
i = 1
while i <= 9:
    casas.append(" ")
    i += 1
jogada = 1
while jogada <= 10:
    for indice, valor in enumerate(casas):
         if indice != 2 and indice  != 5 and indice != 8:
            print(f" {valor} |", end="")
         else:
             print(f" {valor} ")
             if indice != 8:
                print("---|---|---")

 # Win condition

    velha = []
    if jogada >= 5:
        #horizontais
        velha.append(casas[0] != " " and casas[0] == casas[1] and casas[0] == casas[2])
        velha.append(casas[3] != " " and casas[3] == casas[4] and casas[3] == casas[5])
        velha.append(casas[6] != " " and casas[6] == casas[7] and casas[6] == casas[8])
        #Verticais
        velha.append(casas[0] != " " and casas[0] == casas[3] and casas[0] == casas[6])
        velha.append(casas[1] != " " and casas[1] == casas[4] and casas[1] == casas[7])
        velha.append(casas[6] != " " and casas[2] == casas[5] and casas[2] == casas[8])
        #Diagonais
        velha.append(casas[0] != " " and casas[0] == casas[4] and casas[0] == casas[8])
        velha.append(casas[2] != " " and casas[2] == casas[4] and casas[2] == casas[6])
    if True in velha:
        print(f"Velha, {jogador}")
        exit()



#Gameplay
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

    while jogada < 10:
        casa = int(input("Escolha uma casa: "))
        if casa < 1 or casa > 9:
            print(f"{casa} Não é uma casa valida")
        elif casas[casa - 1] != " ":
            print(f"{casa} ja esta ocupada")
        else:
            break


    casas[casa - 1] = jogador
    jogada += 1
    if jogada < 10:
        print(f"\n" * 5)






print("Empate")