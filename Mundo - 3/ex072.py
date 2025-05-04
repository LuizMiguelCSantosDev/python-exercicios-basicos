num_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoite', 'Dezenove', 'Vinte')

while True:
    num_int= int(input('Digite um número entre 0 e 20: '))

    if(num_int >= 0 and num_int <= 20):
        print(f'O número digitado foi {num_int}, ele escrito por extenso é: {num_extenso[num_int]}')
        
    else:
        print('Valor inválido.')

    escolha= str(input('Deseja continuar?[S/N]: ')).upper()
    if(escolha == 'N'):
        break