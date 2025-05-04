times= ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atético-GO', 'Santos', 'Ceará-SC', 'Internacional', 'São Paulo', 'Athlético-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos colocados são: {times[16:]}')
print('-=' * 15)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-=' * 15)

if ('Chapecoense' in times):
    print(f'A Chapecoense está na { times.index('Chapecoense') + 1 }ª posição na tabela')
else:
    print('A Chapecoense não está presente na tabela do Brasileirão Série A')


