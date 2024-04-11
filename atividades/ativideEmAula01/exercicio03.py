'''Escreva um programa em Python que solicite ao usuário dois númerosinteiros ele sempre
 realizará a subtração do maior pelo menor, não importandoa ordem.'''

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    sub1 = num1 - num2
    print(f"resultado da subtração é: {sub1}")
else:
    sub2 = num2 - num1
    print(f"resultado da subtração é: {sub2}")

    