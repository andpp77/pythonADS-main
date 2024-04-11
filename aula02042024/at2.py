# \n = nova linha
print("Diaria Simples = S | Diária Dupla = D | Diária Tripla = T")
tipoDiaria = input("Digite o tipo de diária: ").upper()
quantidadeDiaria = int(input("Digite a quantidade de diárias: "))


if tipoDiaria == ("S"):
    print("Simples - R$255.50")
    calcuDiaria = 255.50 * quantidadeDiaria
    print(f"Valor final a pagar é {calcuDiaria}")
elif tipoDiaria == ("D"):
    print("Dupla - R$305.50")
    calcuDiaria = 305.50 * quantidadeDiaria
    print(f"Valor final a pagar é {calcuDiaria}")
elif tipoDiaria == ("T"):
    print("Tripla - R$360.50")
    calcuDiaria = 360.50 * quantidadeDiaria
    print(f"Valor final a pagar é {calcuDiaria}")
else:
    print("Tipo de diária invalida")