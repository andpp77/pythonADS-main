salario = float(input("Digite o seu salário por mês: "))
horas = float(input("Digite a hora semanal: "))
horaTrabalhada = salario / horas
horaExtra = (horaTrabalhada - (60/100))

print("Sua hora trabalhada é: ", horaTrabalhada)
print("Sua hora Extra é: ", horaExtra)
