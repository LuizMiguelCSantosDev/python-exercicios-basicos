ano= int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 400 == 0):
    print('{} é um ano BISSEXTO'.format(ano))
else:
    print('{} não é um ano BISSEXTO'.format(ano))

