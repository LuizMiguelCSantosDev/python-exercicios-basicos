def escreva(mensagem, tamanho):
    print('~' * tamanho)
    print(f'{mensagem:^{tamanho}}')
    print('~' * tamanho)

mensagem= str(input('Digite a mensagem: '))
escreva(mensagem, len(mensagem)+ 4)