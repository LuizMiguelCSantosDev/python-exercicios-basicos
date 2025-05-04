v= float(input('Digite a velocidade do carro: '))

if (v <= 80):
    print('Você está dentro do limite de velocidade e não foi multado')
else:
    print('Você foi multado')
    multa= (v - 80) * 7
    print('A multa irá custar {:.2f} R$'.format(multa))

print('Tenha um bom dia! Dirija com segurança')