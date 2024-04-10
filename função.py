nomes = ["A", "B", "C"]

print(f"{len(nomes)}: {nomes}")

nomes.append("D")
print(f"append(D) {nomes}")

nomes.sort()
print(f"nomes.sort() {nomes}")

nomes.reverse()
print(f"nomes.reverse {nomes}")

nomes.insert(2, "A")
print(f"nomes.insert(2, A) {nomes} ")

nomes.remove("A")
print(f"nomes.remove(A) {nomes}")

print(f"{nomes.pop(3)}")
print(f"nomes.pop(3) {nomes}")


print(nomes.count("A"))
print(f"nomes.count(A)")

copiado = nomes.copy()
print(f"copy() {copiado}")

print("C" in nomes)
print("D" in nomes)
