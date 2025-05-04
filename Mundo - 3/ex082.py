nums= []
nums_par= []
nums_impar= []

while True:
    num= int(input('Digite um número: '))
    nums.append(num)
    
    while True:
        escolha= str(input('Deseja continuar?[S/N]: ')).upper()
        if(escolha != 'S' and escolha != 'N'):
            print('Opção inválida')
        else:
            break
    
    if(escolha == 'N'):
        break

for num in nums:       
    if(num % 2 == 0):
        nums_par.append(num)
    else:
        nums_impar.append(num)

print(f'A lista de números digitados foi: {nums}')
print(f'A lista de númeres PARES digitados foi: {nums_par}')
print(f'A lista de números ÍMPARES digitados foi: {nums_impar}')