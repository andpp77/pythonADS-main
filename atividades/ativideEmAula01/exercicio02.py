''' Escreva um programa em Python que solicite a entrada de 2 notas dealunos e exiba
 qual é a maior (desconsidere notas iguais).'''

num1 = float(input("Digite o primeiro nota: "))
num2 = float(input("Digite o segundo nota: "))

if num1 > num2:
    print(f"O maior numero é:{num1}")
elif num1 == num2:
    print(f"valores iguais")
else: 
    print(f"O maior numero é:{num2}")