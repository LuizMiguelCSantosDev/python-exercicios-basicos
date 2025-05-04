from random import randint
from time import sleep
from operator import itemgetter

jogadores= dict()
ranking= list()

for i in range(1, 5):
    jogadores[f'Jogador {i}']= randint(1, 6)

print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(1)
    print(f'    O {k} tirou {v} no dado.')

sleep(1)

print('\n   == RANKING DOS JOGADORES ==')

ranking= sorted(jogadores.items(), key = itemgetter(1), reverse=True)

for i, v in enumerate(ranking):    
    sleep(1)
    print(f'    {i+1}º Lugar: {v[0]} com {v[1]}.')
    
   


