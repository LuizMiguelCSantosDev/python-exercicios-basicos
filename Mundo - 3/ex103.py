def ficha(nome= '<desconhecido>', gols= 0):
    
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')


nome= str(input('Nome do Jogador: ')).strip()
gols= str(input('Número de Gols: ')).strip() 


if(len(nome) == 0 and len(gols) == 0):
    ficha()
elif(len(nome) == 0):
    if(gols.isnumeric() == True):
        ficha(gols=gols)
    else:
        ficha()
elif(len(gols) == 0):
    ficha(nome=nome)
else:
    ficha(nome, gols)