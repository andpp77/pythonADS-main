'''NOMES:
Gabriel Da Rocha Prospero
Anderson Santiago De Lima
João Vitor Silva Figueroa
'''
resp = "s"

while resp == "s" or resp == "S":
    decimal = int(input("Digite um numero em Base Decimal: "))
    print("Conversor de base Decimal! \n para Binário = 1 \n para Hexadecimal = 2 \n para Octadecimal = 3")
    conversor = int(input("Escolha uma opção de conversão de base: "))
    if conversor == 1:
        numeroDecimal = decimal
        quociente = 1
        listaResto = []
        while quociente >= 1:
            resto = decimal%2
            listaResto.insert(0,resto)
            quociente = decimal // 2
            decimal = quociente
        binario = ''.join([str(item) for item in listaResto])
        print(f"O numero em Base 10 |{numeroDecimal}|convertido em binário base 2 é igual a |{binario}|")
    elif conversor == 2:
        numeroDecimal = decimal
        base16 = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
        resto = list()
        while decimal > 0:
            resto.append(base16[(decimal % 16)])
            decimal = decimal // 16
        resto.reverse()
        hexa = ''.join([str(item) for item in resto])
        print(f"O numero em Base 10 |{numeroDecimal}|convertido em Hexadecimal base 16 é igual a {hexa}")      
    elif conversor == 3:
        numeroDecimal = decimal
        quociente = 1
        listaResto = []
        while quociente >= 1:
            resto = decimal%8
            listaResto.insert(0,resto)
            quociente = decimal // 8
            decimal = quociente
        octal = ''.join([str(item) for item in listaResto])
        print(f"O numero em Base 10  |{numeroDecimal}| convertido em octal base 8 é igual a |{octal}|") 
    else:
        print("Opção invalida")
    resp = input("Deseja fazer outra conversão?: ")
print("Muito obrigado")