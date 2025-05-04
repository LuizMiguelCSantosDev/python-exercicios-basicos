produtos= ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 10.00, 'Estojo', 12.75, 'Caneta', 1.50)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(len(produtos)):
    if (pos % 2 == 0):
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')

print('-' * 40)

