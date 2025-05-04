import requests

try:
    requests.get('https://www.pudim.com.br/')
except:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site do Pudim com sucesso!')
