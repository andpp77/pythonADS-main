'''3 - Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados 
os dadosde idade e salário. Faça um algoritmo que informe:
a) a média de idade do grupo;
b) a média de salários das pessoas com mais de 40 anos;
c) quantidade de pessoas com salário abaixo de R$2000,00.
Encerre a entrada de dados quando for digitada uma idade negativa 
(os dados da idadenegativa não podem entrar nos cálculos dos itens solicitados acima).'''
#item a
mediaIdade = 0 
contador1 = 0
#item b
mediaSalario = 0
contador2 = 0
#item c
qtde = 0

while True:
    idade = int(input("Digite sua Idade: "))
    Salario = float(input("Digite seu salario: "))
    if idade > 0:
        break
    mediaIdade = mediaIdade + idade
    contador1 = contador1 + 1
    if idade >= 40:
        mediaSalario = mediaSalario = Salario
        contador2 = contador2 + 1
    if Salario < 2000:
        qtde = qtde + 1
if mediaIdade > 0:
    media = mediaIdade/contador1
    media2 = mediaSalario/contador2

    print("Media das idades:", media)
    print("Salário medio das pessoas com >= 40:", media2)
    print("Quantidade de pessoas com salario < 2000:",qtde)



