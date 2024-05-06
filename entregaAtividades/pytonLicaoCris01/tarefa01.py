'''Escreva um programa em Python para calcular o valor de uma prestação em atraso(prestacao).
 Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem demulta pelo 
atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar ovalor da 
prestação atualizado, sabendo que: prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)'''

print("Calcule o valor da prestação")
valorPrestacao = float(input("Digite o valor da prestação: "))
dias = float(input("Digite a quantidade de dias: "))
multa = float(input("Digite o valor da multa: "))

resultado = valorPrestacao + (valorPrestacao*(multa/100)*dias)

print("O valor da prestação é: ", resultado)
