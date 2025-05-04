pos3 = 0
numspar= 0

nums= (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: '))
       )

print(f'O número 9 apareceu um total de: {nums.count(9)} vez(es)')

if (3 in nums):
    print(f'O número 3 foi digitado pela primeira vez na posição: {nums.index(3) + 1}')
else:
    print(f'O número 3 não foi digitado.')

print('Os números pares digitados foram: ', end='')
for num in nums:
    if (num % 2 ==0):
        print(num, end=' ')
        
   
