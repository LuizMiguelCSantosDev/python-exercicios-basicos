vcasa= float(input('Valor da casa: '))
salarioc= float(input('Salário do comprador: '))
anos= int(input('Quantos anos vai pagar: '))

pmensal= vcasa/(anos * 12)
print('O valor da parcela mensal é: {:.2f} R$'.format(pmensal))
if (pmensal <= (salarioc * 0.3)):
    print('O empréstimo foi concedido.')
else:
    print('O empréstimo foi negado')