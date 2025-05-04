from time import sleep

def mostra_linha():
    print('-='*20)

def contador(inicio, fim, passo):
    
    if(passo == 0):
        passo= 1

    
    if(passo < 0):
        passo *= -1
    
    mostra_linha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(2.5)

    if(inicio < fim):
        cont= inicio
        while cont <= fim:      
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
    else:
        cont=inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

mostra_linha()
print('Agora é a sua vez de personalizar a contagem!')
inicio= int(input('Início: '))
fim= int(input('Fim: '))
passo= int(input('Passo: '))
contador(inicio, fim, passo)