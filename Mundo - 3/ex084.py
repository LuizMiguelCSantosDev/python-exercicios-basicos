nome_peso= list()
dados= list()
maiorp = menorp = 0
primeira_vez= True

while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if(primeira_vez == True):
        maior_peso= dados[1]
        menor_peso= dados[1]
        primeira_vez = False
    else:
        if(dados[1] > maior_peso):
            maior_peso= dados[1]
        
        if(dados[1] < menor_peso):
            menor_peso= dados[1]
    
    nome_peso.append(dados[:])
    dados.clear()

    escolha = str(input("Quer continuar?[S/N]: ")).upper()
    if(escolha in 'Nn'):
        break

print(f'Ao todo foram cadastradas {len(nome_peso)} pessoas')
print(f'O maior peso foi de {maior_peso:.1f}Kg. Peso de',end=' ')
for pessoa in nome_peso:
    if(pessoa[1] == maior_peso):
        print(f'[{pessoa[0]}] ', end=' ')
print(f'\nO menor peso foi de {menor_peso:.1f}Kg. Peso de', end=' ')
for pessoa in nome_peso:
    if(pessoa[1] == menor_peso):
        print(f'[{pessoa[0]}] ', end=' ')



