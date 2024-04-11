'''Escreva um programa em Python que solicite ao usuário o valor da compra e o códigoreferente
a forma de pagamento. Calcule e mostre o valor a ser pago. Caso o códigoreferente a forma de 
pagamento seja igual a 1, o algoritmo deve conceder 10% dedesconto, caso contrário 5%'''

print("Mercado Dia: Faça as suas compras!!")
valCompra = float(input("Digite o valor da sua compra: "))
formPagamento = float(input("Digite o codigo referente a forma de pagamento: "))

if formPagamento == 1:
    desconto10 = valCompra *(10/100)
    valComDesconto10 = valCompra - desconto10
    print("forma de pagamento com desconto de 10%")
    print(f"desconto {desconto10}")
    print(f"Valor a pagar {valComDesconto10}")
else:
    desconto5 = valCompra *(5/100)
    valComDesconto5 = valCompra - desconto5
    print("forma de pagamento com desconto de 5%")
    print(f"desconto {desconto5}")
    print(f"Valor a pagar {valComDesconto5}")

