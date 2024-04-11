valor = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite a parcela: "))

if parcelas == 2:
    valJuros = (valor + valor * (3/100))/2
    print("valor das parcelas com juros é ", valJuros)
elif parcelas == 4:
    valJuros = (valor + valor * (7/100))/2
    print("valor das parcelas com juros é ", valJuros)
elif parcelas == 6:
    valJuros = (valor + valor * (7/100))/2
    print("valor das parcelas com juros é ", valJuros)
