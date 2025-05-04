salario= float(input('Digite seu salário: '))

if(salario > 1250.00):
    salario= salario * 1.10
else:
    salario= salario * 1.15

print('O valor do salário após o aumento é: {:.2f} R$'.format(salario))