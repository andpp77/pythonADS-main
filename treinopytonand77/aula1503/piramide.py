print("Calcule o volume do tronco de uma pirâmide:")
bmaior = float(input("Digite o valor da base Maior da Pirâmide: "))
bmenor = float(input("Digite o valor da base Menor da Pirâmide: "))
altura = float(input("Digite o valor da base Menor da Pirâmide: "))

volume = altura/3*(bmaior**2 + bmenor**2 +(bmaior**2*bmenor**2)**0.5)

print("o valor do volume é:", volume)


