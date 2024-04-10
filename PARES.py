primos = [2]
numero = 3
quan = 0

while quan < 5 or quan > 20:
    quan = int(input("Escolha Uma quantidade de primos (5min 20max)  = "))
    if quan < 5 or quan > 20:
        print(f"A Quantidade {quan} é Invalida")


I = 1
while I < quan:
    divisor = 2
    composto = False

    while divisor < numero:
        if numero % divisor == 0:
            composto = True
            break
        else:
            divisor += 1


    if composto == False:
      primos.append(numero)
      I += 1

    numero += 2

print(primos)

