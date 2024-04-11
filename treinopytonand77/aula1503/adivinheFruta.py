import random

adivinhe = random.randrange(input("Adivinhe o numero: "))

sorteado = random.randrange(1,3,2)

while True:
    if adivinhe == sorteado:
        print("voce ganhaou")
        break
    else:
        print("voce perdeu")
        break




