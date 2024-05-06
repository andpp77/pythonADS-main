'''3- Faça um programa em Python que obtenha o valor de uma compra, calcular e mostraro valor da compra considerando
o desconto, conforme descrito abaixo:para compras acima de R$ 200 a loja dá um desconto de 20%para as abaixo disso
não tem desconto, mostre o valor da compra'''

print("Mercado Dia: Compras acima de R$ 200 ganham desconto de 20%")
compra = float(input("Digite o valor da compra: "))

if compra >= 200:
    desconto = (compra *(20/100))
    compraFinal = compra - desconto
    print(f"O valor da compra com desconto é R${compraFinal}")
    print(f"O valor de desconto é R${desconto}")
else:
    print("Sem desconto na compra")