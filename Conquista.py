def imprimir_conquista(conquistas, start=1):
    indice = start
    for conquista in conquistas:
        print(f"Conquista {indice} {conquista}")
        indice += 1

conquistas = ["Level1", "level2", "level3"]

imprimir_conquista(conquistas)