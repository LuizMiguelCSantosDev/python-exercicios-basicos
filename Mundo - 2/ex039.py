from datetime import datetime

nascimento= int(input('Digite o seu ano de nascimento: '))
sexo= str(input('Digite seu sexo: ')).title()

if (sexo == 'Feminino'):
    print('No Brasil não é obrigatório o alistamento militar de mulheres')

else:
    ano_atual= datetime.now().year
    idade= ano_atual - nascimento


    if (idade > 18):
        print(f'Você deveria ter se alistado há {idade - 18} ano(s)')
        print(f'Seu alistamento foi em {nascimento+ 18}')
    elif (idade == 18):
        print('Você tem que alistar imediatamente')
    else:
        print(f'Ainda falta(m) {18 - idade} ano(s) para o alistamento')
        print(f'Seu alistamento será em {nascimento + 18}')
