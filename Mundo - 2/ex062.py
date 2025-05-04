posicao= 1
mais_termos= 0
continuar= 'S'

ptermo= int(input('Digite o valor do primeiro termo: '))
razao= int(input('Digite a razão: '))

while (posicao <= 10):
    termo= ptermo + (posicao- 1) * razao
    print(f'{posicao}º termo: {termo}')
    posicao += 1

while (continuar == 'S'):
    continuar= str(input('Deseja mostrar mais alguns termos? [S/N]: '))

    if(continuar == 'S'):
        mais_termos= int(input('Quantos termos a mais quer mostrar?: ')) + mais_termos 
        while (posicao <= (10 + mais_termos)):
                termo= ptermo + (posicao- 1) * razao
                print(f'{posicao}º termo: {termo}')
                posicao += 1

print('FIM')
            

