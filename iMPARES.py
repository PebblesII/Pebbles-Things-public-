import random
from random import randint

impares = list()
i = 0


while i < 5 or i > 20:
    i = int(input("Escolha Uma quantidade de impares (5min 20max)  = "))
    if i < 5 or i > 20:
        print(f"A Quantidade {i} é Invalida")

I = 0
while I < i:
    impar = randint(0, 9) * 2 + 1
    impares.append(impar)
    I += 1




print(impares)

print("Tamanho", len(impares))
print("Maior", max(impares))
print("Menor", min(impares))
print("Soma", sum(impares))
print("Em ordem", sorted(impares))

