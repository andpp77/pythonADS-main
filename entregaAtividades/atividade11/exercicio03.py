'''3- Faça um programa em Python que solicite ao usuário a placa e o valor da multa de 15
carros. As informações obtidas devem ser armazenadas em 2 listas distintas (observe que
cada lista poderá ter apenas 15 itens armazenados e que na posição i das duas listas
ficarão armazenados: a placa i e o valor de venda i, veja exemplo abaixo).
   - É obrigatório o uso de estrutura de repetição e listas.
   - Calcule e mostre e o valor médio de todas as multas e
quantos carros possuem o valor de multa maior ouigual a R$300.00, 
para isso utilize os dados armazenados nas listas descritas anteriormente e
estrutura de repetição.'''

placaCarro = []
valorMulta = []
car = range(15)

for a in car:
    placa = input("Digite a placa do carro: ")
    multa = float(input("Digite o Valor da multa: "))
    placaCarro.append(placa)
    valorMulta.append(multa)
for i,p in enumerate(placaCarro):
    print("| %d | placa | %s | multas | R$%s " %(i + 1, p, valorMulta[i] ))
soma = sum(valorMulta)
media = soma/len(valorMulta)
print("A média das multas é: R$%d" %(media))