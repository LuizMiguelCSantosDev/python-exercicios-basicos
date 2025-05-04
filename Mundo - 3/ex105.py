def notas(*nums, sit=False):
    '''
    -> Função para analisar n notas de n alunos.
    \n:param: nums= Recebe uma, várias ou nenhuma nota de alunos.
    \n:param: sit= Determina se a situação da turma, determinada de acordo com a média, será parte do dicionário ou não. Por padrão começa como False.
    \n:return: Retorna um dicionário com os campos total, maior, menor e media sendo obrigatórios, e com o campo situação, sendo opcional (ele será mostrado se sit for passado como True).
    '''
    maior = menor = contnotas= media= 0
    for num in nums:
        if(contnotas == 0):
            maior= num
            menor= num
        else:
            if(num > maior):
                maior= num
            
            if(num < menor):
                menor= num

        media += num
        contnotas += 1
    
    if(contnotas != 0):
        media= media/contnotas

    dicionario= {
        'Total': contnotas,
        'Maior': maior,
        'Menor': menor,
        'Média': round(media, 2),
    }

    if(sit == True):
        if(media >= 7):
            dicionario['Situação']= 'BOA'
        elif(media >= 6):
            dicionario['Situação']= 'RAZOÁVEL'
        else:
            dicionario['Situação']= 'RUIM'

    return dicionario

resposta= notas(9.5, 6.0, 7.2, 8.0, 10.0, sit=True)
print(resposta)

print(notas(8.5, 9.0, 10.0, 7.8, sit=True))
print(notas(sit=True))
print(notas())
print(notas(5.0, 4.8, 3.5, 5.2, 6.0, sit=True))
print(notas(6.5, 7.0, 6.2, 5.8, sit=True))