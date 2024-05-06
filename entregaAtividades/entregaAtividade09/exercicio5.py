'''5- Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo 
e aaltura de cada pessoa, calcule e mostre a altura média das mulheres e dos 
homens separadamente. Utilize o comando de repetição que desejar'''
contadorF = 0
contadorM = 0
m = 0
f = 0
resp = 's' 

while resp == 's' or resp == 'S': 
    sexo = input("Digite seu Sexo: ex( m = Masculino / f = Feminino): ")
    altura = float(input("Digite a sua altura: "))
    if sexo == "m":
        h = (72.7 *altura) - 58
        m = m + altura
        contadorM = contadorM + 1
    elif sexo == "f":
        h = (62.1 * altura) - 44.7 
        f = f + altura
        contadorF = contadorF + 1
    else:
        print("Digite uma opçao valida")
        h = 0 
    if h != 0:
        print("Seu peso ideal é: %.2f" %(h),"kg")
    else:
        print("Digite uma altura valida!")
    resp = input("Deseja continuar (s = sim / n = não): ")
mediaM = m/contadorM
mediaF = f/contadorF
print(f"Quantidade de homens é {contadorM}")
print("Media de altura de homens é %.2f" %(mediaM))
print(f"Quantidade de mulheres é {contadorF}")
print("Media de altura de mulheres é %.2f" %(mediaF))
print("valeu")
