from math import cos, sin, tan, radians

angulo= float(input('Digite o valor do ângulo: '))

cosseno= cos(radians(angulo))
seno= sin(radians(angulo))
tangente= tan(radians(angulo))

print('O seno do número é: {:.2f}'.format(seno))
print('O cosseno do número é: {:.2f}'.format(cosseno))
print('A tangente do número é: {:.2f}'.format(tangente))


