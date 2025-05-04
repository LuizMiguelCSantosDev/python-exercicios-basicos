from time import sleep

def mostra_linha():
    print('-='*20)

def soma(*nums):

    mostra_linha()
    print('Analisando os valores passados: ')
    for  num in nums:
        sleep(1)
        print(f'{num} ', end='', flush=True)
    
    print(f'Foram informados {len(nums)} valores ao todo.')
    if(len(nums) > 0):
        print(f'O maior valor informado foi: {max(nums)}.')
    else:
        print(f'O maior valor informado foi: 0.')

soma(2, 4, 6)
soma(10, 20)
soma(5, 15, 25, 35)
soma(7,)
soma(1, 3, 5, 7, 9)
soma()
