import argparse


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
    tempo = 0
    if steps:
#         while len(conteudo[0]) != 0:
#                if conteudo[i][2] < conteudo[menor_tempo][2]:
#                     menor_tempo = i
#             if acumulador != '':
#                 acumulador = acumulador + '->' + conteudo[menor_tempo][1]
#             else:
#                 acumulador = conteudo[menor_tempo][1]
#             print(acumulador)
#             input()
#             del (conteudo[menor_tempo])
#             menor_tempo = 0
    else:
        #usando bubble sort para ordenar o vetor
        for i in range(len(conteudo[0])):
            for j in range(len(conteudo[0])-1):
                if int(conteudo[j][2]) > int(conteudo[j+1][2]):
                    aux = conteudo[j]
                    conteudo[j] = conteudo[j+1]
                    conteudo[j + 1] = aux
        print(conteudo)

        while len(conteudo[0] != 0):
            while tempo <


    return 'func fifo'


def sjf():
    return 'func sjf'


def interativo():
    return 'interativo'


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
    parser.add_argument('--nome_arquivo', "-p", type=str, help='Define o nome do arquivo a ser utilizado',
                        required=True)
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
        elif variaveis.algoritmo == 'interativo':
            interativo(LerArquivo(conteudo), variaveis.steps)
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
