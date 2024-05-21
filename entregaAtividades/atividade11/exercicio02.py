'''2- Faça um programa em Python que contenha 3 listas com os nomes: valores, par e
impar. Solicite N números inteiros ao usuário e armazene-os na lista chamada valores
(utilize como critério de parada se o usuário deseja continuar).
   - Após a obtenção dos dados, na lista par armazene apenas os números pares da lista
valores e na lista ímpar os números ímpares. É obrigatório o uso de estrutura de
repetição e listas.
   - Exiba os números armazenados nas 3 listas.'''

valores = []
par = []
impar = []
contador = 0
resp = "s"

while resp == "s" or resp == "S":
    numeros = int(input("Digite um numero inteiro: "))
    contador = contador + 1
    if numeros % 2 == 0:
        par.append(numeros)
        valores.append(numeros)
    else:
        impar.append(numeros)
        valores.append(numeros)
    resp = input("Deseja continuar?: ")
print("Os valores digitados são :", valores)
print("numeros par", par)
print("numeros impar", impar)
