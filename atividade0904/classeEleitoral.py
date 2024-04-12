nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 16:
    print(f"{nome} Não eleitor")
elif idade > 18 and idade <= 65:
    print(f"{nome} Eleitor obrigatório")
else:
    print(f"{nome} Eleitor Facultativo")