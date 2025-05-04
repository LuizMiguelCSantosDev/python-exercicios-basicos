maiorpeso= 0
menorpeso= 9999 #Poderia usar um if para validar se fosse primeira iteração
for i in range(0, 5):
    peso= float(input('Digite o seu peso (kg): '))

    if(peso > maiorpeso):
        maiorpeso= peso
    if(peso < menorpeso):
        menorpeso= peso

print(f'O maior peso lido foi: {maiorpeso}')
print(f'O menor peso lido foi: {menorpeso}')