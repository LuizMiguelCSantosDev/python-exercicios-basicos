lista_dicionarios= list()
dicionario= dict()
media = 0
mulheres= list()
mmedia= list()

while True:
    dicionario['Nome']= str(input('Nome: '))
    while True:
        sexo= str(input('Sexo [M/F]: ')).upper()
        if(sexo not in 'MmFf'):
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            dicionario['Sexo']= sexo
            break
    
    dicionario['Idade']= int(input('Idade: '))

    media += dicionario['Idade']
    lista_dicionarios.append(dicionario.copy())
    dicionario.clear()

    while True:
        escolha= str(input('Quer continuar?[S/N]: ')).upper()
        if(escolha  not in 'SsNn'):
            print('ERRO! Por favor, digite apenas S ou N.')
        else:
            break
    
    if(escolha in 'Nn'):
        break                  

print('-=' * 35)
print(f'- O grupo tem {len(lista_dicionarios)} pessoas.')

media= float(media/(len(lista_dicionarios)))
print(f'A média de idade é de {media} anos.')

for pessoa in lista_dicionarios:
    if(pessoa["Idade"] > media):
        mmedia.append(pessoa)
    
    if(pessoa["Sexo"] == 'F'):
        mulheres.append(pessoa["Nome"])

print(f'As mulheres cadastradas foram: ', end='')
for mulher in mulheres:
    print(f'{mulher}', end=' ')

print(f'\nAs pessoas com idade acima da média são: ')
for pessoa in mmedia:
    for k, v in pessoa.items():
        print(f'{k} = {v}', end='; ')

    print()
print('<<ENCERRADO>>')   
    

    