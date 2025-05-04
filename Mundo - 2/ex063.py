contador= 0
resposta= [0, 1]
num= int(input('Digite um número: '))

print(max(resposta))
print(min(resposta))

while (contador < num - 2):
    contador += 1
    novo_valor= resposta[len(resposta) - 2] + resposta[len(resposta) -1]
    resposta.append(novo_valor)

print(resposta)

