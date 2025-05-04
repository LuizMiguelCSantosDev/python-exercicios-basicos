matriz= list()
lista_aux= list()

for i in range(3):
    for j in range(3):
        lista_aux.append(input(f'Digite um valor para [{i}, {j}]: ') )
    
    matriz.append(lista_aux[:])
    lista_aux.clear()

print("-="*8)
print(f'{"Matriz 3 X 3":^16}')
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end='')
    
    print()

