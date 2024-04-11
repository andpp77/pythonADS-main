import math
num = float(input("Digite um numero até 10: "))

absoluto = math.fabs(num)
parteinteira = math.trunc (num)
raizquad = math.sqrt (absoluto) 
fatorial = math.factorial (math.trunc(absoluto))

print("O valor absoluto é:", absoluto)
print("O valor da parte inteira é:", parteinteira)
print("O valor da raiz quadrada é:", raizquad)
print("O valor fatorial é:", fatorial)
