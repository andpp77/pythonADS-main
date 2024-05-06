'''2- Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação 
de segundograu, apresentando: as duas raízes, quando for possível efetuar o cálculo 
(delta positivo ouzero); a mensagem "Não há raízes reais", se não for possível fazer 
o cálculo (deltanegativo); e a mensagem "Não é equação do segundo grau", se o valor 
de a for igual azero.'''
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

def bhaskara(a,b,c):
  delta = (b**2) - (4*a*c)
  x1 = (((-1)*b) + (delta**0.5))/(2*a)
  x2 = (((-1)*b) - (delta**0.5))/(2*a)
  if delta == 0:
    print()
    print("A 2º Grau É ",a,".x²",b,".x",c,"= 0")
    print("Como Delta = 0, temos um único valor de raiz (X1 = x2): ",x1)
  elif delta > 0:
    print()
    print("A 2º Grau É ",a,".x²",b,".x",c,"= 0")
    print("Como Delta é maior que 0, temos dois valores distintos de raízes: ",x1,"e",x2)
  else:
    print()
    print("A 2º Grau É ",a,".x²",b,".x",c,"= 0")
    print("Como Delta é menor que 0, não temos raízes reais!")
bhaskara(a,b,c)