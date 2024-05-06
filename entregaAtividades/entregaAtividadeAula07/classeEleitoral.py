'''1- Criar um algoritmo que leia a idade de uma pessoa e informe sua classe eleitoral:
• não-eleitor (abaixo de 16 anos)• eleitor obrigatório (entre 18 e 65 anos)• eleitor 
facultativo (entre 16 e 18 anos e maior de 65 anos)'''

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 16:
    print(f"{nome} Não eleitor")
elif idade > 18 and idade <= 65:
    print(f"{nome} Eleitor obrigatório")
else:
    print(f"{nome} Eleitor Facultativo")