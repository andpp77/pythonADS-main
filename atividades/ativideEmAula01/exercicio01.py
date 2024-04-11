'''Escreva um programa em Python que solicite ao usuário o valor do denominador de
 uma fração, caso seja negativo mostre “valor inválido”'''

num1 = float(input("Digite o denominador: "))

if num1 <= 0:
    print(f"valor invalido: {num1}")
else:
    print(f"valor valido: {num1}")



