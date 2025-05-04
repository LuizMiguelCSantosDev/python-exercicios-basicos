from random import randint
from time import sleep

jogos= list()
aposta= list()

num= int(input("Quantos jogos você quer que eu sorteie?: "))

for j in range(num):
    i= 0
    while (i < 6):
        num_sort= randint(1, 60)
        if (num_sort not in aposta):
            aposta.append(num_sort)
            i += 1
    
    jogos.append(aposta[:])
    aposta.clear()

for j in range(num):
    print(f"Jogo {j+1}: {sorted(jogos[j])}")
    sleep(1)

print("Boa Sorte!!!")





