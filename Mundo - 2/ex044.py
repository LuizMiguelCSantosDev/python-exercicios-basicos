preco= float(input('Digite o preço do produto: '))

print('1 - À vista dinheiro/cheque = 10% de desconto ')
print('2 - À vista no cartão = 5% de desconto')
print('3 - 2x no cartão = Preço Normal ')
print('4 - 3X ou mais no cartão = 20% de juros')
opcao= int(input('Escolha uma das condições de pagamento acima: '))

if (opcao == 1):
    vpago= preco * 0.90
    print(f'O valor a ser pago pelo produto é: {vpago} R$')
elif (opcao == 2):
    vpago= preco * 0.95
    print(f'O valor a ser pago pelo produto é: {vpago} R$')
elif (opcao == 3):
    print(f'O valor a ser pago pelo produto é: {preco} R$')
elif (opcao == 4):
    vpago= preco * 1.20
    print(f'O valor a ser pago pelo produto é: {vpago} R$')
else:
    print('Opção inválida.')