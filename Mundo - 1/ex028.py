nome= input('Digite seu nome: ').strip()

nomediv= nome.split()

print('Primeiro nome= {}'.format(nomediv[0]))
print('Último nome= {}'.format(nomediv[len(nomediv) - 1]))