def leiaInt(texto):
    while True:
        try:
            num = int(input(texto))
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return 0
        except:
            print('ERRO: por favor, digite um número inteiro válido.')
        else:
            return num

def leiaFloat(texto):
    while True:
        try:
            num = float(input(texto))
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return 0
        except:
            print('ERRO: por favor, digite um número inteiro válido.')
        else:
            return num

num_int = leiaInt('Digite um número inteiro: ')
num_float = leiaFloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {num_int} e o real foi {num_float}')