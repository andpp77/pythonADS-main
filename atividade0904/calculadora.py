val01 = float(input("Digite o Primeiro valor: "))
val02 = float(input("Digite o segundo valor: "))
print("Soma '=' + | Subtração = '-' | Multiplicação = '*' | Divisão = / ")
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
    calculo = val01 - val02
    print(f"Resultado é {calculo}")
