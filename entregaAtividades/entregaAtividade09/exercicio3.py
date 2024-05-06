'''3- Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e 
mostre a seguinte soma:S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n'''
s = 1
n = int(input("Digite um numero: "))
for a in range(1, n):
    soma = s + 1/n
print(soma)
