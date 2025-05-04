nums= []

while True:
    nums.append(int(input('Digite um número: ')))
    while True:
        escolha= str(input('Deseja continuar?[S/N]: ')).upper()
        if(escolha != 'N' and escolha != 'S'):
            print('Opção inválida')
        else:
            break
    
    if(escolha == 'N'):
        break

print(f'Foram digitados {len(nums)} número(s)')
print(f'A lista ordenada de forma decrescente é: {sorted(nums, reverse= True)}')
if (5 in nums): 
    print('O valor 5 está na lista') 
else: 
    print('O valor não 5 está na lista')

    