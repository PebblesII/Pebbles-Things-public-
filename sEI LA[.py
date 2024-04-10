#funcao print(), input(), int()
#metodo "Texto".upper()

print("Texto".upper())
print("TEXTO".lower())

nome = "gustavo"
nomeM = nome.upper()

print(nome, nomeM)


def imprimir():
    print("Ola Mundo")

imprimir()

def imprimirComparanmteses(nome):
    print(f"Ola {nome}")

imprimirComparanmteses("Mundo")
imprimirComparanmteses("A")

def imprimirComretorno(n1,n2):
    return n1 * n2

retornado = imprimirComretorno(2, 6)

print(retornado)

