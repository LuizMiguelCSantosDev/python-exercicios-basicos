sair= False

n1= float(input('Digite o primeiro valor: '))
n2= float(input('Digite o segundo valor: '))

while (sair == False):
    print('----- MENU -----')
    print(' [1] Somar ')
    print(' [2] Multiplicar')
    print(' [3] Maior')
    print(' [4] Novos números')
    print(' [5] Sair do programa')

    opcao= int(input('Digite sua opção: '))

    if (opcao == 1):
        print(f'O resultado da soma entre {n1} e {n2} é: {n1+n2}')

    elif (opcao == 2):
        print(f'O resultado da multiplicação entre {n1} e {n2} é: {n1 * n2}')

    elif (opcao == 3):

        if (n1 > n2):
            print('O primeiro valor é maior')
        elif(n2 > n1):
            print('O segundo valor é maior')
        else:
            print('Os dois valores são iguais')

    elif(opcao == 4):
        n1= float(input('Digite o novo valor para o primeiro número: '))
        n2= float(input('Digite o novo valor para o segundo número: '))
    
    elif(opcao == 5):
        sair = True
    else:
        print('Opção inválida, tente novamente')
