'''4- Elabore um programa em Python que implemente uma calculadora com as funções desomar, 
subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os doisvalores, e 
perguntar qual a operação pretendida (+, - , * ou / ) e a seguir calcular emostrar o 
resultado.'''

val01 = float(input("Digite o primeiro valor: "))
val02 = float(input("Digite o segundo valor: "))
print("Soma = '+' | Subtração = '-' | Multiplicação = '*' | Divisão = '/' ")
operacao = (input("Digite a operação matemática: "))

if operacao == ("+"):
    calculo = val01 + val02
    print(f"Resultado é {calculo}")
elif operacao == ("-"):
    calculo = val01 - val02
    print(f"Resultado é {calculo}")
elif operacao == ("*"):
    calculo = val01 * val02
    print(f"Resultado é {calculo}")
elif operacao == ("/"):
    calculo = val01 / val02
    print(f"Resultado é {calculo}")
else:
    print("Digite uma operação válida")