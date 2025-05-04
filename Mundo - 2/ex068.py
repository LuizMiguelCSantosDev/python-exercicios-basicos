from random import randint
vitorias= 0

while True:
    validate_escolha= False
    while (validate_escolha == False):
        escolha= str(input('Par ou Impar[P/I]: '))
        if(escolha == 'P' or escolha == 'I'):
            validate_escolha= True

    jogada_jogador= int(input('Digite um valor: '))
    jogada_computador= randint(0, 10)
    soma= jogada_jogador + jogada_computador
    print(f'Você escolheu {jogada_jogador} e o computador escolheu {jogada_computador} a soma foi {soma}')

    if(escolha == 'P'):
        if(soma % 2 == 0):
            print('Parabéns, você ganhou.')
            vitorias += 1
        else:
            print('Que pena você perdeu.')
            break
    else:
        if(soma % 2 != 0):
            print('Parabéns, você ganhou.')
            vitorias += 1
        else:
            print('Que pena você perdeu.')
            break

print(f'Você venceu por {vitorias} vez(es) consecutiva(s)')
