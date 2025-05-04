n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))

media= ((n1+n2)/2)

if(media >= 7):
    print('Aprovado')
    print(f'Sua média foi: {media}')
elif(media >=5 and media <7):
    print('Recuperação')
    print(f'Sua media foi: {media}')
else:
    print('Reprovado')
    print(f'Sua media foi: {media}')