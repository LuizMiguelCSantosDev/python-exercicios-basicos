estatisticas= dict()
gols_partida= list()

estatisticas['Nome']= str(input('Nome do Jogador: '))
cont= int(input(f'Quantas partidas {estatisticas["Nome"]} jogou? '))

for i in range(0, cont):
    gols_partida.append(int(input(f'    Quantos gols na partida {i+1}? ')))

estatisticas['Gols']= gols_partida[:]
estatisticas['Total']= sum(gols_partida)

print('-=' * 30)
for k, v in estatisticas.items():
    print(f'O campo {k} tem valor {v}')

print('-=' * 30)
print(f'O jogador {estatisticas["Nome"]} jogou {cont} partidas')
for i in range(0, cont):
    print(f'    => Na partida {i+1}, fez {gols_partida[i]} gols.')
print(f'Foi um total de {estatisticas["Total"]} gols.')