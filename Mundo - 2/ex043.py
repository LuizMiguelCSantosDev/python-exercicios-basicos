peso= float(input('Digite seu peso (kg): '))
altura= float(input('Digite sua altura (m): '))

imc= peso/(altura * altura)

if (imc < 18.5):
    print(f'Abaixo do peso. Seu IMC é: {imc}')
elif (imc >= 18.5 and imc < 25):
    print(f'Peso ideal. Seu IMC é: {imc}')
elif (imc >= 25 and imc < 30):
    print(f'Sobrepeso. Seu IMC é: {imc}')
elif (imc >=30 and imc <= 40):
    print(f'Obesidade. Seu IMC é: {imc}')
elif (imc > 40):
    print(f'Obesidade mórbida. Seu IMC é: {imc}')
