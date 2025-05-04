d= float(input('Digite a distância da viagem em KM: '))

if (d <= 200):
    preco= d * 0.50
else:
    preco= d * 0.45

print('O preço da passagem será {:.2f} R$'.format(preco))