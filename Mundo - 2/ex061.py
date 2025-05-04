posicao= 1

ptermo= int(input('Digite o valor do primeiro termo: '))
razao= int(input('Digite a razão: '))

while posicao <= 10:
    termo= ptermo + (posicao- 1) * razao
    print(f'{posicao}º termo: {termo}')
    posicao += 1

