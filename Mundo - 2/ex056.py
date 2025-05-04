somai= 0
hvelho=0
nomehvelho= 'Não há homens entre as pessoas lidas'
contm= 0
for i in range(1, 5):
    print(f'----- {i}ª Pessoa -----')
    nome= str(input('Digite seu nome: '))
    idade= int(input('DIgite sua idade: '))
    sexo= str(input('Digite seu sexo [M/F]: '))

    somai += idade

    if(sexo == 'M'):
        if(idade > hvelho):
            nomehvelho= nome
    else:
        if(idade < 20):
            contm += 1
    
print(f'A média de idade do grupo é: {float(somai/4)}')
print(f'O nome do homem mais velho é: {nomehvelho}')
print(f'Entre as pessoas lidas, {contm} mulher(es) têm menos de 20 anos')
