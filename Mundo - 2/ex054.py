from datetime import date
maioridade=0
nmaioridade=0

for i in range(0, 7):
    nascimento= int(input('Digite o seu ano de nascimento: '))
    idade= date.today().year - nascimento

    if(idade >= 21):
        maioridade += 1
    else:
        nmaioridade += 1

print(f'Das 7 pessoas: \n {nmaioridade} pessoa(s) não atingiu/atingiram a maioridade \n {maioridade} pessoa(s) atingiram a maioridade')


