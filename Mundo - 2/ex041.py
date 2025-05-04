from datetime import datetime

ano_nascimento= int(input('Digite o seu ano de nascimento: '))
idade= (datetime.now().year) - ano_nascimento

if (idade > 25):
    print('A sua categoria é: MASTER')
elif (idade > 19 and idade <= 25):
    print('A sua categoria é: SÊNIOR')
elif (idade > 14 and idade <= 19):
    print('A sua categoria é: JÚNIOR')
elif (idade > 9 and idade <= 14):
    print('A sua categoria é: MIRIM')
else:
    print('A sua categoria é: INFANTIL')