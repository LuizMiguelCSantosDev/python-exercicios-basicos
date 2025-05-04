from random import randint
acerto = False
tentativas= 0
escolha_computador= randint(0, 10) 

while (acerto == False):
    escolha_joogador= int(input('Escolha um número entre 0 e 10: '))
    tentativas += 1
    if(escolha_joogador == escolha_computador):
        print(f'Parabéns, você acertou. Foi necessário {tentativas} tentiva(s) para vencer')
        acerto= True
    else:
        print('Você errou, tente novamente')



