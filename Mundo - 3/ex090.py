aluno= dict()

aluno['Nome']= str(input('Nome: '))
aluno['Média']= float(input(f'Média de {aluno['Nome']}: '))

if(aluno['Média'] >= 7):
    aluno['Situação']= 'Aprovado'
elif (aluno['Média'] >= 5):
    aluno['Situação']= 'Recuperação'
else:    
    aluno['Situação']= 'Reprovado'

print('-=' * 8)    
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
