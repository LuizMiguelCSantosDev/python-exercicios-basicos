nome_notas_media= list()
dados=list()
lista_notas= list()

while True:
    dados.append(str(input("Nome: ")))
    for i in range(1, 3):
        lista_notas.append(float(input(f"Nota {i}: ")))
    
    dados.append(lista_notas[:])
    dados.append(sum(lista_notas)/2)
    nome_notas_media.append(dados[:])

    lista_notas.clear()
    dados.clear()

    escolha=(str(input("Quer continuar?[S/N]: ")))
    if(escolha in 'Nn'):
        break

print("-=" * 26)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')


for i in range(len(nome_notas_media)):
    print(f"{i:<4}{nome_notas_media[i][0]:<10}{nome_notas_media[i][2]:>8.1f}")


while True:
    escolha=int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if(escolha < 0):
        print("Valor inválido")

    if(escolha == 999):
        print("Volte Sempre!!!")
        break

    print(f"Notas de {nome_notas_media[escolha][0]} são {nome_notas_media[escolha][1]}")





