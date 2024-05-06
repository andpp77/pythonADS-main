'''Escreva um programa em Python que solicite ao usuário a distância entre duas cidades e
o tempo de viagem. O programa deverá calcular e exibir a velocidade média de umcarro
que vai de uma cidade para outra. Utilize a fórmula:'''

distancia = float(input("Digite a distancia entre as cidades: "))
tempoViagem = float(input("Digite o tempo de viagem: "))

velMedia = distancia/tempoViagem

print("A velocidade média é: ", velMedia)