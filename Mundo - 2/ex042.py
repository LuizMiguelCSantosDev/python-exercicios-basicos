a= float(input('Digite o valor da primeira reta: '))
b= float(input('Digite o valor da segunda reta: '))
c= float(input('Digite o valor da terceira reta: '))

if (a + b > c and b + c > a and a + c > b):
    if (a == b):
        if (a == c):
            print('O triângulo será EQUILÁTERO, todos os lados são iguais')
        else:
            print('O triângulo será ISÓCELES, dois lados iguais')
    elif (b == c):
        print('O triângulo será ISÓCELES, dois lados iguais')
    else:
        print('O triângulo será ESCALENO, nenhum dos lados iguais')
else:
    print('As retas NÃO PODEM FORMAR um triângulo')