from math import trunc

numero= int(input('Digite um número: '))
milhar= trunc(numero/1000)
subtrair= milhar * 1000
centena= trunc(((numero - subtrair)/100))
subtrair= subtrair + centena * 100
dezena= trunc(((numero - subtrair)/10))
subtrair= subtrair + dezena * 10
unidade= numero - subtrair

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
