from random import choice

escolha_usuario= str(input('Escolha com qual você vai jogar: ')).capitalize()
escolha_computador= choice(['Pedra', 'Papel', 'Tesoura'])
print(f'O computador escolheu: {escolha_computador}')

if (escolha_usuario == escolha_computador):
    print('Empate')
else:
    if(escolha_usuario == 'Papel'):
        if(escolha_computador == 'Pedra'):
            print('Você ganhou')
        else:
            print('Você perdeu')
    elif(escolha_usuario == 'Pedra'):
        if(escolha_computador == 'Papel'):
            print('Você perdeu')
        else:
            print('Você ganhou')
    elif(escolha_usuario == 'Tesoura'):
        if(escolha_computador == 'Papel'):
            print('Você ganhou')
        else:
            print('Você perdeu')
    else:
        print('Jogada inválida')
