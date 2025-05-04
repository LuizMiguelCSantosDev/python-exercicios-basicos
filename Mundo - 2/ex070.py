totalgasto = pmais1000 = maisbarato = 0
primeiravez= True

while True:
    validate_escolha= False
    nomeprod= str(input('Digite o nome do produto: ')).title()
    preco= float(input('Digite o preço: R$'))
    totalgasto += preco

    if(primeiravez == True or preco < maisbarato):
        maisbarato= preco
        nmaisbarato= nomeprod
        primeiravez= False
    
    if (preco > 1000):
        pmais1000 += 1

    while (validate_escolha == False):
        escolha= str(input('Deseja continuar? [S/N]: ')).upper()
        if (escolha == 'S' or escolha == 'N'):
            validate_escolha= True
    
    if (escolha == 'N'):
        break

print(f'O total gasto na compra foi: R${totalgasto:.2f}')
print(f'O número de produtos que custam mais de R$1000 reias é: {pmais1000}')
print(f'O nome do produto mais barato é: {nmaisbarato}. Esse produto custou: R${maisbarato:.2f}')
    

    

    

