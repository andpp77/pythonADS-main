''' Escreva um programa em Python que solicite ao usuário os valores de três contas deconsumo (p.ex. água, luz e telefone)
e o valor de seu salário. Verifique se o salário ésuficiente para pagar as três contas, caso não seja apresente a mensagem
“Salárioinsuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas.'''

nome = input("Digite seu nome: ")
salario = float(input("Digite o valor do seu salário: "))
contaAgua = float(input("Digite o valor da conta de água: "))
contaLuz = float(input("Digite o valor da conta de luz: "))
contaTelefone = float(input("Digite o valor da conta de telefone: "))
pagamento = (salario - contaAgua - contaLuz - contaTelefone)

if pagamento < 0.0:
    print(f"{nome} seu salário é Insuficiente")
else:
    print(f"{nome} seu salário é Suficiente")
    print(f"Sobrou R${pagamento}")
    

