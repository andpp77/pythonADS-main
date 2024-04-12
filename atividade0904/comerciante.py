'''3- Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
Crie uma programa que permita digitar o nome do produto e valor da compra, 
eimprimindo o nome do produto e o valor da venda.'''

produto = input("Digite o nome do produto: ")
compra = float(input("Digite o valor da compra: "))

if compra < 10:
    lucro = (compra * (70/100))
    print(f"Seu produto é {produto}")
    print(f"O valor da venda é {lucro}")
elif compra >= 10 or compra < 30 :
    lucro = (compra * (50/100))
    print(f"Seu produto é {produto}")
    print(f"O valor da venda é {lucro}")
elif compra >= 30 or compra < 50 :
    lucro = (compra * (40/100))
    print(f"Seu produto é {produto}")
    print(f"O valor da venda é {lucro}")
else:
    lucro = (compra * (30/100))
    print(f"Seu produto é {produto}")
    print(f"O valor da venda é {lucro}")


