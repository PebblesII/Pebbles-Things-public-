nomes = []
while True:
    nome = (input("Digite um nome(N para terminar):  "))
    if nome == "N": break
    nomes.append(nome)


i = 0
while i < len(nomes):
    nome = nomes[i]
    print(f"[ {i}- {nome}", end= "]")
    print()
    i +=1



Buscar = input("Digite o nome que quer buscar : ")


if Buscar in nomes:
    print()
else:
    print(f"Não Achado {Buscar}")
    exit()

i = 0
while i < len(nomes):
    nome = nomes[i]
    if nome == Buscar:
        print(f"Achado {Buscar} No indice {i}")
        exit()
    i += 1
print(f"Não achado na {Buscar} Em {nomes}")
