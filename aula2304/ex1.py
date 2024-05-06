'''1- Faça um programa em Python que recebe a idade de cada um dos 5 alunos de uma escola, 
matriculados no Ensino Médio. O algoritmo deverá,usando estrutura de repetição, verificar, 
calcular e imprimir:
a) a quantidade de alunos que podem votar, ou seja, têm idade mínima de 16anos.
b) a média da idade dos alunos que não são eleitores.'''

qtdeEleitores = 0
soma = 0
qtdeNEleitores = 0

for alunos in range(5):
    idade = int(input("Digite a sua idade: "))
    if idade < 16 :
        qtdeNEleitores = qtdeNEleitores + 1
        soma = soma + idade
    else:
        qtdeEleitores = qtdeEleitores +1
media = soma/qtdeNEleitores
print("A quantidade de Eleitores: ",qtdeEleitores)
print("A quantidade de não Eleitores: ",qtdeNEleitores)
print("Media de idade dos alunos Não eleitores",media)

    