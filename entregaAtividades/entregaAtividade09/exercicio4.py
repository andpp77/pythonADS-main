'''4- Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são positivos e quantos são negativos. Determine, também, qual é o menor 
dessesvalores. Utilize o comando de repetição que desejar.'''
numPositivo = 0
numNegativo = 0
soma = range(10)
maior = 0
menor = 0
contador = 0
for n in soma:
    numero = float(input("Digite um numero: "))
    contador = contador + 1
    if numero < 0:
        numNegativo = numNegativo + 1     
    elif numero >= 0:
        numPositivo = numPositivo + 1 
    if contador ==  1:
        maior = numero
        menor = numero 
    else:  
       if numero > maior:
        maior = numero
       if numero < menor:
        menor = numero
print("O numero de valores positivos é : ", numPositivo)
print("O numero de valores negativos é : ", numNegativo)
print("O menor numero é : ", menor)
print("O maior numero é : ", maior)


