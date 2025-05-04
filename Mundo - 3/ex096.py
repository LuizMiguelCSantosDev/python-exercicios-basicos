def titulo():
    print('-'*25)
    print(f'{"Controle de Terrenos":^25}')
    print('-'*25)


def area(largura, comprimento):
    print(f'A área de um terreno {largura}x{comprimento} é de {largura*comprimento}m².')


titulo()
largura= float(input('Largura (m): '))
comprimento= float(input('Comprimento (m): '))
area(largura, comprimento)
