frase= input('Digite uma frase: ').strip()
frase= frase.upper()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A') +1))
print('A letra A aparece pela ultima vez na posição {}.'.format(frase.rfind('A') + 1))