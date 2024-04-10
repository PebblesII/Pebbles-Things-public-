import time

Nome = input("seu nome é =")
Altura = int(input("sua altura é ="))

print("nome", Nome, "Altura", Altura)
time.sleep(1)

print("Nome{} Altura{}".format(Nome, Altura))
time.sleep(1)

print(f"Nome {Nome} Altura {Altura}")