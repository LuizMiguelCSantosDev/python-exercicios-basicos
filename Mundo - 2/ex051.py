ptermo= float(input('Digite o primeiro termo da PA: '))
razao= float(input('Digite a razão: '))

for num in range(1, 11):
    print(f'{num}º Termo: {ptermo + ((num - 1)*razao)}')