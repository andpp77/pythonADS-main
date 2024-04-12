nome = input("Digite seu nome: ")
media = float(input("Digite sua media: "))
frequencia = float(input("Digite sua frequencia: "))

if frequencia < 75:
    print(f"{nome} Reprovado por falta")
elif media < 6:
    print(f"{nome} reprovado por nota")
else:
    print(f"{nome} aprovado!!!")