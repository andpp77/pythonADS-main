num = int(input("Digite um numero com 3 digitos: "))
#Primeiro digito
d1 = num // 100
print("Primeiro Digito: ", d1)
#Segundo digito
d2 = num % 100 // 10
print("Segundo Digito: ", d2)
#Terceiro digito
d3 = num % 10
print("Terceiro digito: ", d3)
#Numero Invertido
inverso = d3 * 100 + d2 * 10 + d1
print("numero invertido = ", inverso)