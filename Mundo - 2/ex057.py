valorcorreto= False

while (valorcorreto == False):
    sexo= str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if(sexo =='M' or sexo =='F'):
        valorcorreto= True
    else:
        print('Você digitou um valor que não é válido. Tente Novamente')
        
print(f'O seu sexo é: {sexo}')

