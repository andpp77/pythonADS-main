contador = 0
soma = 0
resp = 's'

while resp == 's' or resp == 'S':
    n = int(input("Digite um numero: "))
    soma = soma + n
    contador = contador + 1
    resp = input("Deseja continuar (s = sim / n = não)")

media = soma/contador
print("Média = ", media)