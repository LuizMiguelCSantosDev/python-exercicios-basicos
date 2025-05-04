while True:

    num= int(input('Qual número quer saber a tabuada: '))
    if(num < 0):
        break

    print('-' * 30)
    for i in range (11):
        print(f'{num} x {i} = {num * i}')
    print('-' * 30)

print('Fim do programa')
