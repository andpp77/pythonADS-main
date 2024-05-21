nomes = []
for i in range(5):
    n = input("Digite um nome: ")
    nomes.insert(i,n)

print(nomes)

for i in range(len(nomes)):
    print(nomes[i])

print(nomes[2])
nomes.sort()
print(nomes)