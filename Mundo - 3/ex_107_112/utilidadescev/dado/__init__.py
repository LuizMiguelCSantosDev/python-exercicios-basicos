def leiaDinheiro(texto):
    while True:
        preco = input(texto)

        # Verifica se a string está vazia ou começa com ',' ou '.'
        if preco == '' or preco[0] in ',.':
            print(f'ERRO: "{preco}" é um preço inválido!')
            continue

        # Verifica se a string contém apenas números, vírgulas ou pontos
        valido = True
        for char in preco:
            if not (char.isdigit() or char in ',.'):
                valido = False
                break
        
        #Formata a string para ter ponto, o que a permite ser convertida para float
        if valido:
            return float(preco.replace(',', '.'))
        
        print(f'ERRO: "{preco}" é um valor inválido!')


#Forma de fazer mais resumida usando REGEX, pedi ajuda do ChatGPT:
import re
def leiaDinheiro_REGEX(texto):
    while True:
        preco = input(texto).strip()

        if (preco == ''):  # Verifica se está vazio
            print(f'ERRO: "{preco}" é um preço inválido!')
            continue

        # Expressão regular para validar números com opcionalmente um separador decimal (ponto ou vírgula)
        if re.fullmatch(r"\d+([.,]\d*)?", preco):  
            return float(preco.replace(',', '.'))  # Converte a vírgula em ponto e retorna o valor
        else:
            print(f'ERRO: "{preco}" é um preço inválido!')

           


