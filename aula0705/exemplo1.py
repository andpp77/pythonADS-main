nomes = []
for i in range(5):
    n = input("Digite um nome: ")
    nomes.append(n)

print(nomes)
for p in nomes:
    print(nomes(p), end="")

for x,e in enumerate(nomes):
    print("[%d] - %s" %((x+1, e)))