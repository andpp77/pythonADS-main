import math
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / math.pow(altura,2)

if imc < 20:
    print("%.2f Seu indice de massa corpória é " %(imc))
    print("Você está abaixo do peso")
elif imc >= 20 and imc < 25 :
    print("%.2f Seu indice de massa corpória é "  %(imc))
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("%.2f Seu indice de massa corpória é " %(imc))
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("%.2f Seu indice de massa corpória é " %(imc))
    print("Obeso")
else:
    print("%.2f Seu indice de massa corpória é " %(imc))
    print("Obeso Morbido")
