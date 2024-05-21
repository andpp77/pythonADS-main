#inverte uma string

invertido = '' #variavel auxiliar - string
texto = input("Digite um texto: ")

for letra in texto:
    invertido = letra + invertido

if invertido ==  texto:
    print(f"{texto} texto é palíndrome")
else:
    print(f"{texto} texto não é palíndrome")