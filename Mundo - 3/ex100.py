from random import randint
from time import sleep

def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        numeros.append(randint(1, 10))
        sleep(1)
        print(f'{numeros[i]}', end=' ', flush=True)
        i += 1
    print('PRONTO!')

def somaPar(numeros):
    somapares= 0
    for num in numeros:
        if(num % 2 == 0):
            somapares += num
    print(f'Somando os valores pares de {numeros}, temos {somapares}')



numeros= list()
sorteia(numeros)
somaPar(numeros)