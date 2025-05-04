from ex_115.lib.interface import cores, leia_int, leia_texto
import os

# Caminho para criar o arquivo dentro da pasta ex_115
PASTA_ATUAL = os.path.dirname(__file__)
PASTA_EX_115 = os.path.abspath(os.path.join(PASTA_ATUAL, '..', '..'))
CAMINHO_CADASTROS = os.path.join(PASTA_EX_115, 'Cadastros.txt')


def dados_pessoa():
    nome = leia_texto('Nome: ')
    idade = leia_int('Idade: ')
    return nome, idade


def cadastrar(nome, idade):
    try:
        with open(CAMINHO_CADASTROS, 'a') as arquivo:
            arquivo.write(f'{nome};{idade}\n')
    except Exception as erro:
        print(f'{cores("vermelho")}Erro ao manipular o arquivo de dados: {erro}{cores("sem")}')
    else:
        print(f'Novo registro de {cores("branco")}{nome}{cores("sem")} adicionado.')


def listar():
    try:
        with open(CAMINHO_CADASTROS, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                pessoa = linha.strip().split(';')
                print(f'{pessoa[0]:<41}{pessoa[1]} ano(s)')
    except FileNotFoundError:
        print(f'{cores("vermelho")}Nenhum cadastro encontrado ainda.{cores("sem")}')
    except Exception as erro:
        print(f'{cores("vermelho")}Erro ao ler os dados: {erro}{cores("sem")}')
