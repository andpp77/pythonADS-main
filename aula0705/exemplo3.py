nros = []
soma = 0
qtde = 0
while True:
    nro = int(input("Digite um numero: "))
    if nro == 0:
        break
    nros.append(nro)
# acumula valores
soma = sum(nros)
# calcula media  
media = soma/len(nros)
# conta quantos valores estao acima da media
for i in nros:
    if i > media:
        qtde +=  1
print("media", media)
print("acima da media:", qtde)