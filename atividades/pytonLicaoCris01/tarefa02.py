'''Escreva um programa em Python que solicite ao usuário o salário atual e mostre o salário
acrescido de 5% de comissão. Sabendo que: comissao = salario*5/100'''

print("Descubra seu salário com comissão")
salario = float(input("Digite o valor do seu salário: "))

calculo = salario * (5/100)

comissao = salario + calculo

print("O valor do salário com comissão é: ", comissao)