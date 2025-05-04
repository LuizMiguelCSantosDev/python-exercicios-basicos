def titulo(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'{texto:^{tamanho}}')
    print('~' * tamanho)

def imprimir_manual(comando):
    from time import sleep
    
    sleep(1)
    help(comando)
    sleep(1)

while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    escolha= str(input('Função ou Biblioteca (FIM para parar)> '))

    if(escolha.upper().strip() != 'FIM'):
        titulo(f"Acessando o manual do comando '{escolha}' ")
        imprimir_manual(escolha)
    else:
        titulo('ATÉ LOGO!')
        break