valores= []
while True:
    num= int(input('Digite um número: '))
    if(num not in valores):
        valores.append(num)
        print('Valor adicionado')
    else:
        print('O valor já existe na lista e por isso não será adicionado')
    
    escolha= str(input('Deseja continuar inserindo valores?[S/N]: ')).upper()
    if(escolha == 'N'):
        break

print(f'Os valores que você digitou, em ordem crescente, foram: {sorted(valores)}')