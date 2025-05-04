valores= []

for i in range(5):
    valores.append(int(input('Digite um valor: ')))

print(f'O maior valor digitado foi {max(valores)} na posição ', end='')
for pos,valor in enumerate(valores):
    if(valor == max(valores)):
        print(pos, end='... ')

print(f'\nO menor valor digitado foi {min(valores)} na posição ', end='')
for pos, valor in enumerate(valores):
    if(valor == min(valores)):
        print(pos, end='... ')