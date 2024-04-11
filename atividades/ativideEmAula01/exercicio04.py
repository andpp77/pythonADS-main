'''Uma empresa está selecionando entre seus estagiários os que irão fazer um treinamento especial.
O selecionado deve satisfazer ao mesmo tempo a dois critérios.O primeiro critério é que ele deve
ter uma bolsa maior ou igual a R$ 750,00 e menor ouigual a R$ 950,00.O segundo critério leva em
conta o tempo de estágio, este deve ser maior ou igual a 2anos'''

print("Treinamento Especial")
nome = input("Digite seu nome: ")
bolsa = float(input("Digite o valor da sua bolsa: "))
tempoEstagio = float(input("Digite o seu tempo de estágio: "))

if bolsa >= 750 and bolsa <= 950 and tempoEstagio >= 2:
    print("Você atende aos Critérios")
    print("Você foi selecionado a fazer o Treinamento Especial")
else:
    print("Você não atende aos critérios")



