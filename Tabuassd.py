Tab = int(input("Digite um numero = "))
Fim = int(input("Até = "))

while Tab != 0:
    I = 1
    while I <= Fim:
        Resultado = Tab * I
        print("{} X {} = {}".format(Tab, I, Resultado))
        I = I + 1

    print("")
    Tab = int(input("Digite um numero = "))
    Fim = int(input("Até = "))

if Tab != 0:
    print("Bye Bye")