idade = int("Digite sua idade: ")

if idade < 16:
    print("Não eleitor")
elif idade > 18 and idade <= 65:
    print("Eleitor obrigatório")
else:
    print("Eleitor Facultativo")