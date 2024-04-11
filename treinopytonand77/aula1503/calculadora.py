print("Calculadora")
val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
operacao = input("Escolha a operação:")

if operacao == ("+"):
     resultado = val1 + val2
     print("o resultado da soma é: ", resultado)
elif operacao == ("-"):
     resultado = val1 - val2
     print("O resultado da subtração é: ", resultado)
elif operacao == ("*"):
     resultado = val1 * val2
     print("O resultado da multiplicação é", resultado)
elif operacao == ("/"):
     resultado = val1 / val2
     print("o resultado da divisão é", resultado)
else:
     print("digite uma operação valida!")
     
     
     
     
     
     


     



