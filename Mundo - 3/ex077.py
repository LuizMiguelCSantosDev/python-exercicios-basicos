palavras= ('Calendario', 'Estante', 'Computador', 'Teclado', 'Cama')
vogais= ()

for palavra in palavras:
    print(f'\n A palavra {palavra} tem as vogais: ', end='') 
    for char in palavra:
        if (char in 'AaEeIiOoUu'):
            print(char, end=' ')
