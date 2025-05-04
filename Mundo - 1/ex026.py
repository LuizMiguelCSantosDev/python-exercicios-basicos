nome= input('Digite seu nome: ').strip()
nome= nome.upper()
condicao= 'SILVA' in nome

if(condicao == True):
    print('Você tem SILVA no nome')
else:
    print('Você não tem SILVA no nome')