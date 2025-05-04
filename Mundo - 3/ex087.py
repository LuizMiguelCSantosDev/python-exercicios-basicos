matriz= list()
lista_aux= list()
soma_pares= soma_tlinha = maiorvalorl2 = 0

for i in range(3):
    for j in range(3):
        lista_aux.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    
    matriz.append(lista_aux[:])
    lista_aux.clear()

print("-="*8)
print(f'{"Matriz 3 X 3":^16}')
for i in range(3):
    for j in range(3):

        if(matriz[i][j] % 2 == 0):
            soma_pares += matriz[i][j]

        if(j < 2):
            print(f"[ {matriz[i][j]} ]", end='')
        else:
            print(f"[ {matriz[i][j]} ]")
print("-="*8)


print(f"A soma dos valores pares é: {soma_pares}")

for i in range(3):
    soma_tlinha += matriz[i][2]

print(f"A soma dos valores da terceira coluna é: {soma_tlinha}")

for i in range(3):
    if(i == 0):
        maiorvalorl2= matriz[1][i]
    else:
        if(matriz[1][i] > maiorvalorl2):
            maiorvalorl2= matriz[1][i]
        
print(f"O maior valor da segunda linha é: {maiorvalorl2}")

