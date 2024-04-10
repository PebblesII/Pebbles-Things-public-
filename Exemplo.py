#leia dois numeros inteiros e efetue uma soma


print("=" * 30)

print("CALCULADORA ")

print("=" * 30)

print("=" * 30)

print("Qual equação")
print(" +   -   *   M")
print(" 1   2   3   4")

escolha = int(input())

print("=" * 30)

print("=" * 30)

print(" Digite dois números ")

print("=" * 30)

N1 = int(input())
N2 = int(input())

Soma = N1 + N2
Menos = N1 - N2
Vezes = N1 * N2
Média = (N1 + N2) /2


if escolha == 1:
    print("=" * 30)

    print("O Resultado é ", Soma)

    print("=" * 30)

if escolha == 2:
    print("=" * 30)

    print("O Resultado é ", Menos)

    print("=" * 30)

if escolha == 3:
    print("=" * 30)

    print("O Resultado é ", Vezes)

    print("=" * 30)

if escolha == 4:
    print("=" * 30)

    print("A média é ", Média)

    print("=" * 30)


