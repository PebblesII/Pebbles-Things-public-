import random
Nu = 0
Alvo = int(input(" Alvo é = "))
Tentativas = 0

while Nu != Alvo:
    print(Nu)
    Nu = random.randint(0, 9999)
    Tentativas += 1

print("Acerto!")
print(Nu)

print("Numero de tentativas")
print(Tentativas)


escolhidoB = random.randint(0,9)

while True:
    print("Escolha entre 0 a 9")
    escolhidoP = int(input())
    if escolhidoP == escolhidoB:
        print("Acerto!")
        break
    else:
        print("Erro")


aluno = []

i = 1



while i <= 5:
    aluno.append(input("Digite seu nome: "))
    i += 1


sorteado = random.randint(1, 5)
print(f"O aluno escolhido é: {aluno[sorteado]} Seu numero sendo {sorteado}")