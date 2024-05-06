'''2 - Faça um programa em Python que solicite a uma quantidade indeterminada de usuários 
sua altura e sexo (M = Masculino / F = Feminino), calcule e imprima para cada um o seu 
peso ideal. Utilize aseguinte expressão: > Masculino (M): (72.7*h) – 58 > Feminino (F): (62.1*h) – 44.7'''

contador = 0 #contador
soma = 0 #acumulador
resp = 's' #inicialização da variável de controle

while resp == 's' or resp == 'S': 
    sexo = input("Digite seu Sexo: ex( m = Masculino / f = Feminino): ")
    altura = float(input("Digite a sua altura: "))
    if sexo == "m":
        h = (72.7 *altura) - 58
    elif sexo == "f":
        h = (62.1 * altura) - 44.7  
    else:
        print("Digite uma opçao valida")
        h = 0 
    if h != 0:
        print("Seu peso ideal é: %.2f" %(h),"kg")
    else:
        print("Digite uma altura valida!")
    resp = input("Deseja continuar (s = sim / n = não): ")
print("valeu")
