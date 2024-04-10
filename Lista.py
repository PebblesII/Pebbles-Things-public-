import time


Lista = [16, "GameDev", True, 21, 145, 123, 543]

print(Lista[0])
print(Lista[1])
print(Lista[2])

print(f"Tamanho da lista  {len(Lista)}")

contador = 0

while contador < len(Lista):
    time.sleep(1)
    print(Lista[contador])
    contador += 1





