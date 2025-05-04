nome= input('Digite o nome de uma cidade: ').strip()
nomediv= nome.upper().split() 

if (nomediv[0] == 'SANTO'):
    print('A cidade começa com o nome Santo')
else:
    print('A cidade não começa com o nome Santo')