cedulas50 = cedulas20 = cedulas10= cedulas1 = 0
while True:
    vsaque= int(input('Digite o valor a ser sacado: R$'))
    for i in range (4):
        if(i == 0):
            cedulas50= vsaque // 50
            vsaque= vsaque - (cedulas50* 50)    
        elif(i == 1):
            cedulas20= vsaque // 20
            vsaque= vsaque - (cedulas20 * 20)
        elif(i == 2):
            cedulas10= vsaque // 10
            vsaque= vsaque - (cedulas10 * 10)
        elif(i == 3):
            cedulas1= vsaque

        if(vsaque == 0):
            break
    break

print(f'Total de cédulas de R$50: {cedulas50}')
print(f'Total de cédulas de R$20: {cedulas20}')
print(f'Total de cédulas de R$10: {cedulas10}')
print(f'Total de cédulas de R$1: {cedulas1}')

