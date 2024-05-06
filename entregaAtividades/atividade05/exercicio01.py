'''1- Escreva um algoritmo que solicite um número ao usuário. Caso seja digitado um valorentre 0 e 9,
mostre: “valor correto”, caso contrário mostre: “valor incorreto”.'''

numero = int(input("Digite um numero de 0 até 9: "))

if numero <= 9:
    print("Valor está correto")
else:
    print("Valor está incorreto")