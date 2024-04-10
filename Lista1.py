import time

print("pares")
pares = []

pares.append(2)
pares.append(8)

print(pares)
print(len(pares))


print("impares")
impares = [1, 3, 5, 7, 9]
print(impares)
print(len(impares))



Contador = 0

Lista = []

while Contador <= 9:
    Lista.append(Contador * 2 + 1)
    Contador += 1
print(Lista)




Descrição = []

I = False

Answear = input("Test")
if Answear == "Yes":
    I = True


while I == True:

    Descrição.append(input("Se descreva = "))

    print(Descrição)


linha = []

linha.append("Mesagem:")
linha.append("Mesagem:1")
linha.append("Mesagem:2")
linha.append("Mesagem:3")

I = 0
while I < len(linha):
    print(linha[I], end=" ")
    I += 1
print()
print("/" * 30)
print("sai do while")
