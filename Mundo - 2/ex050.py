soma_pares= 0
for i in range(0, 6):
    num= int(input('Digite um número: '))
    if (num % 2 == 0):
        soma_pares += num

print(f'A soma dos números pares foi: {soma_pares}')