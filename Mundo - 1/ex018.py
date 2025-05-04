from math import hypot

co= float(input('Digite o valor do cateto oposto: '))
ca= float(input('Digite o valor do cateto adjacente: '))

hip= hypot(co, ca)

print('O comprimento da hipotenusa será: {:.2f}'.format(hip))