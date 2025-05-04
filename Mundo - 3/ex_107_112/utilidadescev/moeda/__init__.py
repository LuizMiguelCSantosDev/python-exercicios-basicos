def metade(preco=0, formatar=True):
    new_preco= preco/2
    if(formatar == True):
        new_preco= moeda(new_preco)
    return new_preco

def dobro(preco=0, formatar=True):
    new_preco= preco * 2
    if(formatar == True):
        new_preco= moeda(new_preco)
    return new_preco

def aumentando(preco=0, fator_de_aumento=0, formatar=True):
    new_preco = preco + (preco * fator_de_aumento)/100
    if(formatar == True):
        new_preco= moeda(new_preco)
    
    return new_preco
    
def diminuindo(preco=0, fator_de_reducao=0, formatar=True):
    new_preco = preco - (preco * fator_de_reducao)/100
    if(formatar == True):
        new_preco= moeda(new_preco)
    return new_preco

def moeda(preco=0, moeda='R$'):
    preco_formatado= (f'{moeda} {preco:.2f}').replace('.', ',')
    return preco_formatado

def resumo(preco=0, aumento=10, reducao=20):
    print('-' * 34)
    print(f'{"RESUMO DO VALOR":^34}')
    print('-' * 34)

    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}"% de aumento: \t{aumentando(preco, aumento, True)}')
    print(f'{reducao}"% de redução: \t{diminuindo(preco, reducao, True)}')

    print('-' * 34)