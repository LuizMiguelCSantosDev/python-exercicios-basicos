from random import randint

nsorteado= randint(0 ,5) 
nusuario= int(input('Digite um número : '))

print('O numero sorteado pelo computador foi: {}'.format(nsorteado))
if(nusuario == nsorteado):
    print('Parabéns você venceu!')
else:
    print('Que pena, você perdeu!')