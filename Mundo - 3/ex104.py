def leiaint(texto):
    while True:

        print(f'{texto}', end='')
        n= str(input()).strip()

        if(n.isnumeric() == True):
            return n
        else:
            print('ERRO! Digite um número inteiro válido')


n= leiaint('Digite um número: ')
print(f"Você acabou de digitar o número: {n}.")


