import argparse
import os
from fila import Conteudo

# Vamos utilizar o módulo argparse para inserir as variaveis por linha de comando

def LerArquivo(arquivo):
    # Divide_dados é um vetor contendo todas as LINHAS do txt
    divide_dados = arquivo.split('\n')

    # Dados_atomicos vai dividir as linhas do txt em dados separados por ';'
    dados_atomicos = []
    for i in range(len(divide_dados)):
        # insere cada split(divisão) na lista 'dados_atomicos'
        dados_atomicos.append(divide_dados[i].split(';'))
    return dados_atomicos


def fifo(conteudo, steps):
    tempo_total = 0
    tempo_de_entrada = 0
    conteudo_aux = Conteudo()
    
    os.system("cls")
    print('RESULTADO:')
    print('SISTEMA EM LOTE')
    print('ESCALONAMENTO PRIMEIRO A ENTRAR, PRIMEIRO A SAIR\n')
    # usando bubble sort para ordenar o vetor
    for i in range(len(conteudo[0])):
        for j in range(len(conteudo[0]) - 1):
            if int(conteudo[j][2]) > int(conteudo[j + 1][2]):
                aux = conteudo[j]
                conteudo[j] = conteudo[j + 1]
                conteudo[j + 1] = aux

    if steps:
        while True:
            for i in range(len(conteudo)):
                if int(conteudo[i][2]) == tempo_total:                   
                    print(conteudo_aux[0][1] + conteudo_aux.__repr__() + conteudo[i][1] + ' FOI CRIADO')
                    input()
                    conteudo_aux.inserir(conteudo[i])
            if int(conteudo_aux[0][3]) - (tempo_total - tempo_de_entrada) == 0:
                # deleta o processo quando ele finaliza
                conteudo_aux.remover()
                tempo_de_entrada = tempo_total
            if not conteudo_aux.__bool__():
                break
            tempo_total += 1
        
    else:
        acumulador = ''
        while True:
            for i in range(len(conteudo)):
                if int(conteudo[i][2]) == tempo_total:                   
                    if acumulador != '':
                        acumulador += "->" + conteudo[i][1]
                    else:
                        acumulador = conteudo[i][1]
                    conteudo_aux.inserir(conteudo[i])
            if int(conteudo_aux[0][3]) - (tempo_total - tempo_de_entrada) == 0:
                # deleta o processo quando ele finaliza
                conteudo_aux.remover()
                tempo_de_entrada = tempo_total
            if not conteudo_aux.__bool__():
                break
            tempo_total += 1
        print(acumulador)


def sjf(conteudo, steps):
    qtd_dados = len(conteudo)
    tempo_total = 0
    tempo_de_entrada = 0
    acumulador = '0'
    soma_retorno = 0
    conteudo_aux = []
    os.system("cls")  # limpar a tela
    print('RESULTADO:')
    print('SISTEMA EM LOTE')
    print('ESCALONAMENTO TAREFA MAIS CURTA PRIMEIRO\n')

    # usando bubble sort para ordenar o vetor pelo tempo da tarefa de modo crescente


    print('TEMPO DE SUBMISSAO:')

    print('\nTEMPO DE EXECUCAO')
        
    
    
    if steps:
        
           
            
    else:



def rr():
    return 'func rr'


def garantido():
    return 'func garantido'


def loteria():
    return 'func loteria'


def main():
    # definindo a descrição do projeto:
    parser = argparse.ArgumentParser(description='Projeto escalonadores')

    # Buscando os argumentos pelo módulo argparse:
    parser.add_argument('--nome_arquivo', "-p", type=str, help='Define o nome do arquivo a ser utilizado', required=True
                        )
    parser.add_argument('--sistema', "-s", type=str,
                        help='Tipo de sistema: defiene se o sistema é em lote ou interativo. Padrão: lote',
                        default='lote')
    parser.add_argument('--algoritmo', "-a", type=str,
                        help='Define o algoritmo a ser utilizado: fifo ; sjf ; rr ; garantido ; loteria')
    parser.add_argument('--tempo', "-q", type=int, help='Define o quantum em ms dos processos.', default=50)

    # action = 'store_true' guarda 'TRUE', se o parametro for chamado
    parser.add_argument('--steps', help='Ativa o passo-a-passo', action='store_true')

    # colocando os argumentos da linha de comando dentro da variavel 'variaveis'
    variaveis = parser.parse_args()

    # verifica se foi passado parametro para o 'tipo do algoritmo', senao, define os padroes
    if variaveis.algoritmo is None:
        if variaveis.sistema == 'lote':
            variaveis.algoritmo = 'fifo'
        elif variaveis.sistema == 'interativo':
            variaveis.algoritmo = 'rr'

    try:
        with open(variaveis.nome_arquivo) as arq_obj:
            conteudo = arq_obj.read()
    # Caso o arquivo nao abra
    except FileNotFoundError:
        print('Nao foi possivel abrir o arquivo')
        return 0
    # se abrir
    else:

        if variaveis.algoritmo == 'fifo':
            fifo(LerArquivo(conteudo), variaveis.steps)
        elif variaveis.algoritmo == 'sjf':
            sjf(LerArquivo(conteudo), variaveis.steps)
        elif variaveis.algoritmo == 'rr':
            rr(LerArquivo(conteudo), variaveis.steps)
        elif variaveis.algoritmo == 'garantido':
            garantido(LerArquivo(conteudo), variaveis.steps)
        elif variaveis.algoritmo == 'loteria':
            loteria(LerArquivo(conteudo), variaveis.steps)

            # fecha o arquivo
    # finally:
    #   arq_obj.close()

    return 0


if __name__ == '__main__':
    main()
