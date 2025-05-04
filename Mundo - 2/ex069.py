pmais_18 = num_homens = mulheres_menos20 = 0

while True:
    validate_sex= validate_escolha = False

    idade= int(input('Digite a idade: '))
    while (validate_sex == False):
        sexo= str(input('Digite o sexo [M/F]: ')).upper()
        if (sexo == 'M' or sexo == 'F'):
            validate_sex= True

    if(idade >= 18):
        pmais_18 += 1

    if(sexo == 'M'):
        num_homens += 1
    else:
        if(idade < 20):
            mulheres_menos20 += 1

    while (validate_escolha == False):
        escolha= str(input('Deseja inserir mais uma pessoa? [S/N]: ')).upper()
        if(escolha == 'N' or escolha == 'S'):
            validate_escolha= True
    
    if(escolha == 'N'):
        break

print(f'{pmais_18} pessoa(s) têm mais de 18 anos')
print(f'{num_homens} homem(ens) foi/foram cadastrado(s)')
print(f'{mulheres_menos20} mulher(es) têm menos de 20 anos')
