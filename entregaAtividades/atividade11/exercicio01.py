'''1- Faça um programa em Python que solicite ao usuário, enquanto o mesmo desejar,
números e armazene-os em uma lista.
Após a entrada de dados, somar os valores da lista, calcular e mostrar a média.
Calcule e mostre quantos números armazenados na lista estão acima da média.'''

contador = 0
soma = 0
acima = 0
resp = "s"
num = []
while resp == "s" or resp == "S":
    numero = float(input("Digite um numero: "))
    soma += numero
    num.append(numero)
    resp = input("Deseja continuar?: ")
media = soma/len(num)
for acimaMedia in num:  
    if acimaMedia > media:  
        acima += 1 
print("sua media é ", media)
print("Vezes que atingiu acima da média:", acima)
print(num)