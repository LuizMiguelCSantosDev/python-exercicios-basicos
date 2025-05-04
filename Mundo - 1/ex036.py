a= float(input('Digite o valor da primeira reta: '))
b= float(input('Digite o valor da segunda reta: '))
c= float(input('Digite o valor da terceira reta: '))

if (a + b > c and b + c >a and a + c > b):
    print('As retas PODEM FORMAR um triângulo')
else:
    print('As retas NÃO PODEM FORMAR um triângulo')


# Forma de lista:

a= float(input('Digite o valor da primeira reta: '))
b= float(input('Digite o valor da segunda reta: '))
c= float(input('Digite o valor da terceira reta: '))

lista=[a, b, c]
lista.sort()

if (lista[0] + lista[1] > lista[2]):
    print('As retas podem formar um triangulo')
else:
    print('As retas não podem formar um triângulo')
