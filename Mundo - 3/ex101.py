def voto(ano_nascimento):
    from datetime import datetime

    idade= datetime.now().year - ano_nascimento
    if(idade >= 18 and idade < 65):
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif(idade >= 16 or idade >= 65):
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO NEGADO.'

ano_nascimento= int(input('Em que ano você nasceu?: '))
print(voto(ano_nascimento))