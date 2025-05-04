nome= input('Digite seu nome completo: ').strip()

print('O seu nome com todas as letras maiúsculas é: {}'.format(nome.upper()))
print('O seu nome com todas as letras minúsculas é: {}'.format(nome.lower()))

nomediv= nome.split()
nomesep= ''.join(nomediv)

print('O seu nome sem considerar os espaços tem {} letras'.format(len(nomesep)))
print('O seu primeiro nome tem {} letras'.format(len(nomediv[0])))