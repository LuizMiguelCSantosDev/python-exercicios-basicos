cont_numeros= 0
soma= 0
flag= False

while (flag == False):
    num= int(input('Digite um número: '))

    if(num != 999):
        cont_numeros += 1
        soma += num
    else:
        flag = True

print(f'O total de números digitados foi: {cont_numeros}')
print(f'A soma dos números digitados foi: {soma}')

