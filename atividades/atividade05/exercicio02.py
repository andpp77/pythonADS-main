'''2- Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de horas
trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas aseguir, de acordo
com o turno de trabalho. Caso o turno seja igual a N (utilize umcaractere para representar) o valor
da hora trabalhada é R$ 45,00, caso contrário é R$37,50'''

nome = input("Digite seu nome: ")
print("horários: Matutino = m, Vespertino = v, Noturno = n")
turnoTrabalho = input("Digite o seu Turno de trabalho: ")
horaTrabalho = float(input("Digite a hora trabalhada: "))

if turnoTrabalho == ("n"):
    salario = 45.0 * horaTrabalho
    print(nome, f"O seu Salário é R${salario}")
    print(f"O Valor da sua hora trabalhada é R$", 45.0)
elif turnoTrabalho == ("m"):
    salario = 37.5 * horaTrabalho
    print(nome, f"O seu Salário é R${salario}")
    print(f"O Valor da sua hora trabalhada é R$", 37.5)
elif turnoTrabalho == ("v"):
    salario = 37.5 * horaTrabalho
    print(nome, f"O seu Salário é R${salario}")
    print(f"O Valor da sua hora trabalhada é R$", 37.5)
else:
    print("Coloque um turno de trabalho válido!!")


    
    
    
    
    
