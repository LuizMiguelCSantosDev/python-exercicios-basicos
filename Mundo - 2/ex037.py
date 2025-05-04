numero = int(input('Digite um número: '))

print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
escolha= int(input('Escolha qual será a base de conversão: '))

if (escolha == 1):
    numeroconv= bin(numero)
    print(f'{numero} convertido para BINÁRIO é igual a: {numeroconv.replace('0b', '')}')
elif (escolha == 2):
    numeroconv= oct(numero)
    print(f'{numero} convertido para OCTAL é igual a: {numeroconv.replace('0o', '')}')
elif (escolha == 3):
    numeroconv= hex(numero)
    print(f'{numero} convertido para HEXADECIMAL é igual a: {numeroconv.replace('0x', '')}')
else:
    print('Opção inválida, tente novamente.')