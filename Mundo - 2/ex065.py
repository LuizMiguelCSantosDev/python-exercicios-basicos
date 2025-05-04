opcao = 'S'
soma=0
contador= 0

while (opcao == 'S'):
    if (opcao == 'S'):
        numero= int(input('Digite um valor: '))

        if(contador == 0):
            maior = numero
            menor = numero

            soma += numero
            contador += 1
        else:
            soma += numero
            contador += 1

            if(numero > maior):
                maior= numero
            
            if(numero < menor):
                menor= numero

        opcao= str(input('Deseja continuar a digitar mais valores?[S/N]: ')).strip().upper()[0]

print(f'A media entre todos os valores digitados foi: {float(soma/contador)}')
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')
