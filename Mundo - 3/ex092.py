from datetime import datetime

trabalhador= dict()
ano_atual= datetime.now().year

trabalhador['Nome']= str(input('Nome: '))
ano_nascimento= int(input('Ano de Nascimento: '))
trabalhador['Idade']= ano_atual - ano_nascimento
trabalhador['CTPS']= int(input('Carteira de Trabalho (0 se não tem): '))

if(trabalhador['CTPS'] != 0):
    trabalhador['Ano de contratação']= int(input('Ano de contratação: '))
    trabalhador['Salário']= float(input('Salário: R$ '))
    anos_contribuicao= datetime.now().year - trabalhador['Ano de contratação']
    trabalhador['Aposentadoria']= ((trabalhador['Ano de contratação'] - ano_nascimento)+35) 

print('-='*25)
for k, v in trabalhador.items():
    print(f'{k} tem valor {v}')


