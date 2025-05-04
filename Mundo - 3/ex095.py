lista_jogadores= list()
estatisticas= dict()
gols_partida= list()

while True:
    print('-' * 50)
    gols_partida.clear()
    estatisticas.clear()
    estatisticas["Nome"]= str(input('Nome do jogador: '))
    cont= int(input(f'Quantas partidas {estatisticas["Nome"]} jogou? '))
    for i in range(0, cont):
        gols_partida.append(int(input(f'Quantos gols na partida {i}? ')))
    
    estatisticas["Gols"]= gols_partida[:]
    estatisticas["Total"]= sum(gols_partida[:])
    lista_jogadores.append(estatisticas.copy())

    while True:
        escolha= str(input('Quer continuar?[S/N]: '))
        if(escolha in 'SsNn'):
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    
    if(escolha in 'Nn'):
        break

print('-=' * 25)
print('cod ', end='')
for k in estatisticas.keys():
    print(f'{k:<15}', end='')
print()
print('-=' * 25)

for k, v in enumerate(lista_jogadores):
    print(f'{k:>3} ', end='')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()

print('-' * 50)

while True:
    while True:
        escolha= int(input('Mostrar dados de qual jogador?(999 encerra): '))
        if(escolha >= 0 and escolha < len(lista_jogadores) or escolha == 999):
            break
        else:
            print(f'ERRO! Não existe jogador com código {escolha}! Tente Novamente')
        
    if(escolha != 999):
        print(f'--LEVANTAMENTO DO JOGADOR {lista_jogadores[escolha]["Nome"]}:')
        
        for p, gols in enumerate(lista_jogadores[escolha]["Gols"]):
            print(f'\t=> Na partida {p +1 } fez {gols} gols.')

        print('-' * 50)
    else:
        break

print('<<VOLTE SEMPRE>>')
