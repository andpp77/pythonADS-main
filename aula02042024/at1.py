nome = input("Digite seu nome: ")
media = float(input("Digite sua media: "))
frequencia = float(input("Digite sua frequencia: "))

if frequencia < 75:
    print("Reprovado por falta")
elif media < 6:
    print("reprovado por nota")
else:
    print("aprovado!!!")