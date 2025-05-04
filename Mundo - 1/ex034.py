num1= float(input('Digite o primeiro número: '))
num2= float(input('Digite o segundo número: '))
num3= float(input('Digite o terceiro número: '))

if (num1 > num2 and num1 > num3):
    print('O maior número é: {}'.format(num1))
    if(num2 > num3):
        print('O menor número é: {}'.format(num3))
    else:
        print('O menor número é: {}'.format(num2))
else:
    if (num2 > num1 and num2 > num3):
        print('O maior número é: {}'.format(num2))
        if (num1 > num3):
            print('O menor número é: {}'.format(num3))
        else:
            print('O menor número é: {}'.format(num1))
    else:
        print('O maior número é: {}'.format(num3))
        if (num1 > num2):
            print('O menor número é: {}'.format(num2))
        else:
            print('O menor número é: {}'.format(num1))

# Forma de lista:

num1= float(input('Digite o primeiro número: '))
num2= float(input('Digite o segundo número: '))
num3= float(input('Digite o terceiro número: '))

lista= [num1, num2, num3]
lista.sort() 

print('O maior valor é: {}'.format(lista[2]))
print('O menor valor é: {}'.format(lista[0]))