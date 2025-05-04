def fatorial(n=1, show=False):
    '''
    -> Função para calcular o fatorial de um número.
    \n:param: n = O número para ser calculado o fatorial.
    \n:param: show = É opcional, determina se a conta vai ser mostrada ou não.
    \n:return: Retorna o fatorial do número n.
    
    '''
    fatorial= 1
    
    for i in range(n, 0, -1):
        if(show == True):
            print(i, end='')
            if(i == 1):
                print(' = ', end='')
            else:
                print(' x ', end='')

        fatorial *= i

    return fatorial


print(fatorial(5, show=True))
print(fatorial(4, show=False))
print(fatorial(3, show=True))
print(fatorial(1, show=True))
print(fatorial(show=True))
