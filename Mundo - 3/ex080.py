nums= []
primeira_vez = True

for i in range(5):
    valor = int(input('Digite um número: '))
    if(primeira_vez == True):
        nums.append(valor)
        primeira_vez = False
    else:
        add_index= 0
        for num in nums:
            if(valor > num):
                add_index += 1
                
        nums.insert(add_index, valor)

print(f'A lista ordenada é: {nums}')
    









        




    