numero= int(input('Digite um número: '))
iteracao= numero
resposta= 1

if(numero < 0):
    print('Não existe fatorial de números negativos')
else:
    while iteracao > 0:
        resposta *= iteracao
        iteracao -= 1
    
    print(f'O fatorial do número {numero} é: {resposta}')


