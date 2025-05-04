num= int(input('Digite um número: '))
validacao=0
for i in range(1, num+1):
    if (num % i ==0):
        validacao +=1

if (validacao == 2):
    print(f'{num} É um número primo')
else:
    print(f'{num} NÃO É um número primo')