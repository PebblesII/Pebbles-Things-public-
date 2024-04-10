from random import randint

input("Jogue os dados     Enter    ")



d1 = randint(1,6)
d2 = randint(1,6)

resultado = d1 + d2

if resultado == 7:
    print(f"Os dados deram {resultado} Ganho")
else:
    print(f"Os dados deram {resultado} Perda")

