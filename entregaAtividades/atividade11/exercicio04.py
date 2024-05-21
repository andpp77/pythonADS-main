'''4- Criar um programa em Python que leia os dados necessários para cadastrar os nomes
de N alunos em uma lista, em outra lista as respectivas notas dos alunos e em uma
terceira lista o seu curso (ccp ou tads). Observe que na posição i das três listas ficarão
guardados: o nome do aluno i, a nota do aluno i e o curso do aluno i.
Resolva os seguintes itens:
a) Calcule e visualize a quantidade de alunos do curso de tads.
b) Calcule e visualize a média das notas dos N alunos.
c) Quantos alunos estão com a nota acima da média.'''
nomeAluno = []
notaAluno = []
cursoAluno = []
soma = 0
cursoccp = 0
cursotads = 0
resp = "s"

while resp == "s" or resp == "S":
    nomes = input("Digite seu nome: ")
    notas = float(input("Digite a sua Nota: "))
    curso = int(input("Digite qual é o seu curso: ccp = 1 | tads = 2 "))
    if curso == 1:
        cursoAluno.append("ccp")
        nomeAluno.append(nomes)
        notaAluno.append(notas)
        cursoccp = cursoccp + 1
    elif curso == 2:
        nomeAluno.append(nomes)
        notaAluno.append(notas)
        cursoAluno.append("tads")
        cursotads = cursotads + 1
    else:
        print("curso invalido, Cadastre Novamente!")
    resp = input("Deseja continuar cadastrando?: ")
soma = sum(notaAluno)
media = soma/len(notaAluno)
acima = 0
for acimaMedia in notaAluno:  
    if acimaMedia > media:  
        acima += 1   
for i,p in enumerate(nomeAluno):
    print("| %d | Nome | %s | Nota | %s | Curso%s " %(i + 1, p, notaAluno[i], cursoAluno[i] ))
print(f"Quantidade de alunos do curso ccp: {cursoccp}")
print(f"Quantidade de alunos do curso tads: {cursotads}")
print(f"Média de notas dos alunos: {media}")
print(f"Quantidade de alunos Acima da Média: {acima}")
