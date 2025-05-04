frase= str(input('Digite uma frase: ')).replace(' ', '').lower()
ultimo_index= len(frase) - 1
validacao= 0

for i in range(0, len(frase)):
    if(frase[ultimo_index - i] == frase[i]):
        validacao += 1

if(validacao == len(frase)):
    print('A frase É um palindromo')
else:
    print('A frase NÃO É um palindromo')

''' -- Forma simplificada --
if (frase == frase[::-1]):
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')
'''

