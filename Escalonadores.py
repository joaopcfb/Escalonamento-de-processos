import argparse
import os
import random
from fifo_sjf import Conteudo
from rr import Conteudo_rr
from garantido import Conteudo_garant
from loteria import Conteudo_loteria


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
    em_execucao = ['', '', '', 0]
    os.system("cls")
    print('RESULTADO:')
    print('SISTEMA EM LOTE')
    print('ESCALONAMENTO PRIMEIRO A ENTRAR, PRIMEIRO A SAIR\n')
    # usando bubble sort para ordenar o vetor
    #     for i in range(len(conteudo[0])):
    #         for j in range(len(conteudo[0]) - 1):
    #             if int(conteudo[j][2]) > int(conteudo[j + 1][2]):
    #                 aux = conteudo[j]
    #                 conteudo[j] = conteudo[j + 1]
    #                 conteudo[j + 1] = aux
    sorted(conteudo, key=lambda processo: processo[2])
    if steps:
        while True:
            for i in range(len(conteudo)):
                # VERIFICA SE EXISTE UM PROCESSO QUE TEM O TEMPO DE SUBMISSAO IGUAL AO TEMPO ATUAL, SE SIM, INSERE ELE NA LISTA AUXILIAR
                if int(conteudo[i][2]) == tempo_total:
                    print(em_execucao[1] + conteudo_aux.__repr__() + ' ' + conteudo[i][1] + ' FOI CRIADO')
                    input()
                    conteudo_aux.inserir(conteudo[i])
            if int(em_execucao[3]) - (tempo_total - tempo_de_entrada) == 0:
                # poe o processo para executar
                em_execucao = conteudo_aux.executar()
                tempo_de_entrada = tempo_total
            if not em_execucao:
                break
            tempo_total += 1

    else:
        acumulador = ''
        while True:
            for i in range(len(conteudo)):
                # VERIFICA SE EXISTE UM PROCESSO QUE TEM O TEMPO DE SUBMISSAO IGUAL AO TEMPO ATUAL, SE SIM, INSERE ELE NA LISTA AUXILIAR
                if int(conteudo[i][2]) == tempo_total:
                    conteudo_aux.inserir(conteudo[i])
            if int(em_execucao[3]) - (tempo_total - tempo_de_entrada) == 0:
                # poe o processo para executar
                em_execucao = conteudo_aux.executar()
                # Botei a condicao 'em_execucao != None' para nao inserir o valor None no acumulador
                if acumulador != '' and em_execucao != None:
                    acumulador += "->" + em_execucao[1]
                elif em_execucao != None:
                    acumulador = em_execucao[1]
                tempo_de_entrada = tempo_total
            if em_execucao is None:
                break
            tempo_total += 1
        print(acumulador)


def sjf(conteudo, steps):
    qtd_dados = len(conteudo)
    tempo_total = 0
    tempo_de_entrada = 0
    acumulador = '0'
    soma_retorno = 0
    em_execucao = ['', '', '', 0]
    conteudo_aux = Conteudo()
    os.system("cls")  # limpar a tela
    print('RESULTADO:')
    print('SISTEMA EM LOTE')
    print('ESCALONAMENTO TAREFA MAIS CURTA PRIMEIRO\n')

    # usando bubble sort para ordenar o vetor pelo tempo da tarefa de modo crescente
    for i in range(len(conteudo[0])):
        for j in range(len(conteudo[0]) - 1):
            if int(conteudo[j][3]) > int(conteudo[j + 1][3]):
                aux = conteudo[j]
                conteudo[j] = conteudo[j + 1]
                conteudo[j + 1] = aux

    print('TEMPO DE SUBMISSAO:')
    for i in range(len(conteudo)):
        print(str(conteudo[i][1]) + '=' + str(conteudo[i][2]))

    print('\nTEMPO DE EXECUCAO')
    for i in range(len(conteudo)):
        print(str(conteudo[i][1]) + '=' + str(conteudo[i][3]) + 'ms')
    print('\n')

    if steps:
        while True:
            for i in range(len(conteudo)):
                if int(conteudo[i][2]) == tempo_total:
                    print(str(tempo_total) + ':ORDENANDO')  ## Tentar refazer a logica, esta printando em linhas separadas mesmo os que entram no mesmo tempo   #####
                    conteudo_aux.inserir(conteudo[i])
                    conteudo_aux.ordenar_por_job()
                    if em_execucao[1] != '' and em_execucao != None:
                        print(em_execucao[1] + '->' + conteudo_aux.__repr__())
                        input()
                    elif em_execucao != None:
                        print(conteudo_aux.__repr__())
                        input()
            if int(em_execucao[3]) - (tempo_total - tempo_de_entrada) == 0:
                # poe o processo para executar
                if em_execucao[1] != '':
                    acumulador += '--' + str(em_execucao[1]) + '--' + str(int(tempo_de_entrada) + int(em_execucao[3]))
                    print(acumulador)
                    input()
                    soma_retorno += (int(tempo_de_entrada) + int(em_execucao[3]))
                em_execucao = conteudo_aux.executar()

                tempo_de_entrada = tempo_total
            if not em_execucao:
                break
            tempo_total += 1
        print('TEMPO DE RETORNO MEDIO: ')
        print(str(int(soma_retorno / qtd_dados)) + 'ms->' + str(int((soma_retorno / qtd_dados) / 1000)) + 's->' + str(
            int(((soma_retorno / qtd_dados) / 1000) / 60)) + 'm\n')
    else:
        while True:
            for i in range(len(conteudo)):
                if int(conteudo[i][2]) == tempo_total:
                    conteudo_aux.inserir(conteudo[i])
                    conteudo_aux.ordenar_por_job()
            if int(em_execucao[3]) - (tempo_total - tempo_de_entrada) == 0:
                # poe o processo para executar
                if em_execucao[1] != '':
                    acumulador += '--' + str(em_execucao[1]) + '--' + str(int(tempo_de_entrada) + int(em_execucao[3]))
                    soma_retorno += (int(tempo_de_entrada) + int(em_execucao[3]))
                em_execucao = conteudo_aux.executar()
                tempo_de_entrada = tempo_total
            if not em_execucao:
                break
            tempo_total += 1
        print(acumulador)
        print('\nTEMPO DE RETORNO MEDIO: ')
        print(str(int(soma_retorno / qtd_dados)) + 'ms->' + str(int((soma_retorno / qtd_dados) / 1000)) + 's->' + str(
            int(((soma_retorno / qtd_dados) / 1000) / 60)) + 'm\n')


def rr(conteudo, steps, quantum):
    conteudo_aux = Conteudo_rr()
    sorted(conteudo, key=lambda processo: processo[2])
    tempo_total = 0
    tempo_de_entrada = 0
    em_execucao = ['', '', '', 0]
    os.system("cls")  # limpar a tela
    print('RESULTADO:')
    print('SISTEMA EM LOTE')
    print('ESCALONAMENTO ROUND ROBIN\n')
    if steps:
        while True:
            for i in range(len(conteudo)):
                if int(conteudo[i][2]) == tempo_total:
                    conteudo_aux.inserir(conteudo[i])
            if int(em_execucao[3]) - (tempo_total - tempo_de_entrada) == 0:
               # poe outro processo para executar
               finalizado = em_execucao[1]
               em_execucao = conteudo_aux.executar()
               tempo_de_entrada = tempo_total
               if em_execucao:
                   if tempo_total !=0:
                       print("%.2f" %(tempo_total/1000) +'s', '   ', em_execucao[1], '      ', conteudo_aux.__repr__(), finalizado, 'FINALIZADO')
                       input()
                   else:
                       print("%.2f" %(tempo_total/1000) +'s', '   ', em_execucao[1], '      ', conteudo_aux.__repr__())
                       input()
               else:
                   print("%.2f" %(tempo_total/1000) +'s', '   ', '-', '      ', finalizado, 'FINALIZADO')
                   input()
                   break                
            if (tempo_total - tempo_de_entrada) == quantum:
                em_execucao[3] = int(em_execucao[3]) - int(tempo_total - tempo_de_entrada) #quando o tempo do processo for igual ao do quantum, diminuir o tempo que ja foi processado e inserir no final da fila
                conteudo_aux.inserir(em_execucao)
                em_execucao = conteudo_aux.executar()
                print("%.2f" %(tempo_total/1000) +'s', '   ', em_execucao[1], '      ', conteudo_aux.__repr__())
                input()
                tempo_de_entrada = tempo_total
            tempo_total += 1
            #Fazer contar a partir do tempo de entrada
    else:
        while True:
            for i in range(len(conteudo)):
                if int(conteudo[i][2]) == tempo_total:
                    conteudo_aux.inserir(conteudo[i])
            if int(em_execucao[3]) - (tempo_total - tempo_de_entrada) == 0:
               # poe outro processo para executar
               finalizado = em_execucao[1]
               em_execucao = conteudo_aux.executar()
               tempo_de_entrada = tempo_total
               if em_execucao:
                   if tempo_total !=0:
                       print("%.2f" %(tempo_total/1000) +'s', '   ', em_execucao[1], '      ', conteudo_aux.__repr__(), finalizado, 'FINALIZADO')
                   else:
                       print("%.2f" %(tempo_total/1000) +'s', '   ', em_execucao[1], '      ', conteudo_aux.__repr__())
               else:
                   print("%.2f" %(tempo_total/1000) +'s', '   ', '-', '      ', finalizado, 'FINALIZADO')
                   break                
            if (tempo_total - tempo_de_entrada) == quantum:
                em_execucao[3] = int(em_execucao[3]) - int(tempo_total - tempo_de_entrada) #quando o tempo do processo for igual ao do quantum, diminuir o tempo que ja foi processado e inserir no final da fila
                conteudo_aux.inserir(em_execucao)
                em_execucao = conteudo_aux.executar()
                print("%.2f" %(tempo_total/1000) +'s', '   ', em_execucao[1], '      ', conteudo_aux.__repr__())
                tempo_de_entrada = tempo_total
            tempo_total += 1

def garantido(conteudo, steps, quantum):
    conteudo_aux = Conteudo_garant()
    sorted(conteudo, key=lambda processo: processo[2])
    tempo_total = 0
    tempo_de_entrada = 0
    em_execucao = ['', '', '', 0, 0]
    os.system("cls")  # limpar a tela
    print('RESULTADO:')
    print('SISTEMA EM LOTE')
    print('ESCALONAMENTO GARANTIDO\n')
    
    if steps:
        while True:        
                for i in range(len(conteudo)):
                    if int(conteudo[i][2]) == tempo_total:
                        conteudo[i].append(0)
                        conteudo_aux.inserir(conteudo[i])
                if int(em_execucao[3]) - int(em_execucao[4] + int(tempo_total - tempo_de_entrada)) == 0:
                   # poe outro processo para executar
                   em_execucao[4] = em_execucao[4] + int(tempo_total - tempo_de_entrada)
                   finalizado = em_execucao[1]
                   em_execucao = conteudo_aux.executar()
                   tempo_de_entrada = tempo_total
                   if em_execucao:
                       if tempo_total !=0:
                           if em_execucao[4] == 0:
                               print("%.2f" %(tempo_total/1000) +'s', '   ', '('+(em_execucao[1]) +',' + str(0) +')', '      ', conteudo_aux.__repr__(tempo_total), finalizado, 'FINALIZADO')
                               input()
                           else:
                               print("%.2f" %(tempo_total/1000) +'s', '   ', '('+(em_execucao[1]) +',' + str(round((em_execucao[4]/tempo_total),2)) +')', '      ', conteudo_aux.__repr__(tempo_total), finalizado, 'FINALIZADO')
                               input()
                       else:
                           if em_execucao[4] == 0:
                               print("%.2f" %(tempo_total/1000) +'s', '   ', '('+(em_execucao[1]) +',' + str(0) +')', '      ', conteudo_aux.__repr__(tempo_total))
                               input()
                           else:
                               print("%.2f" %(tempo_total/1000) +'s', '   ', '('+(em_execucao[1]) +',' + str(round((em_execucao[4]/tempo_total),2)) +')', '      ', conteudo_aux.__repr__(tempo_total))
                               input()
                   else:
                       print("%.2f" %(tempo_total/1000) +'s', '   ', '-', '      ', finalizado, 'FINALIZADO')
                       input()
                       break                
                if (tempo_total - tempo_de_entrada) == quantum:
                    em_execucao[4] = em_execucao[4] + int(tempo_total - tempo_de_entrada) #quando o tempo do processo for igual ao do quantum, diminuir o tempo que ja foi processado e inserir no final da fila
                    conteudo_aux.inserir(em_execucao)
                    em_execucao = conteudo_aux.executar()
                    print("%.2f" %(tempo_total/1000) +'s', '   ', '('+(em_execucao[1]) +',' + str(round((em_execucao[4]/tempo_total),2)) +')', '      ', conteudo_aux.__repr__(tempo_total))
                    input()
                    tempo_de_entrada = tempo_total
                tempo_total += 1
    else:
        while True:        
            for i in range(len(conteudo)):
                if int(conteudo[i][2]) == tempo_total:
                    conteudo[i].append(0)
                    conteudo_aux.inserir(conteudo[i])
            if int(em_execucao[3]) - int(em_execucao[4] + int(tempo_total - tempo_de_entrada)) == 0:
               # poe outro processo para executar
               em_execucao[4] = em_execucao[4] + int(tempo_total - tempo_de_entrada)
               finalizado = em_execucao[1]
               em_execucao = conteudo_aux.executar()
               tempo_de_entrada = tempo_total
               if em_execucao:
                   if tempo_total !=0:
                       if em_execucao[4] == 0:
                           print("%.2f" %(tempo_total/1000) +'s', '   ', '('+(em_execucao[1]) +',' + str(0) +')', '      ', conteudo_aux.__repr__(tempo_total), finalizado, 'FINALIZADO')
                       else:
                           print("%.2f" %(tempo_total/1000) +'s', '   ', '('+(em_execucao[1]) +',' + str(round((em_execucao[4]/tempo_total),2)) +')', '      ', conteudo_aux.__repr__(tempo_total), finalizado, 'FINALIZADO')
                   else:
                       if em_execucao[4] == 0:
                           print("%.2f" %(tempo_total/1000) +'s', '   ', '('+(em_execucao[1]) +',' + str(0) +')', '      ', conteudo_aux.__repr__(tempo_total))
                       else:
                           print("%.2f" %(tempo_total/1000) +'s', '   ', '('+(em_execucao[1]) +',' + str(round((em_execucao[4]/tempo_total),2)) +')', '      ', conteudo_aux.__repr__(tempo_total))
               else:
                   print("%.2f" %(tempo_total/1000) +'s', '   ', '-', '      ', finalizado, 'FINALIZADO')
                   break                
            if (tempo_total - tempo_de_entrada) == quantum:
                em_execucao[4] = em_execucao[4] + int(tempo_total - tempo_de_entrada) #quando o tempo do processo for igual ao do quantum, diminuir o tempo que ja foi processado e inserir no final da fila
                conteudo_aux.inserir(em_execucao)
                em_execucao = conteudo_aux.executar()
                print("%.2f" %(tempo_total/1000) +'s', '   ', '('+(em_execucao[1]) +',' + str(round((em_execucao[4]/tempo_total),2)) +')', '      ', conteudo_aux.__repr__(tempo_total))
                tempo_de_entrada = tempo_total
            tempo_total += 1

def loteria(conteudo, steps, quantum):
    conteudo_aux = Conteudo_loteria()
    sorted(conteudo, key=lambda processo: processo[2])
    tempo_total = 0
    tempo_de_entrada = 0
    em_execucao = ['', '', '', 0, 0]
    os.system("cls")  # limpar a tela
    print('RESULTADO:')
    print('SISTEMA EM LOTE')
    print('ESCALONAMENTO loteria\n')


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
        ####Fazer separacao de sistemas que sao em lote dos que sao interativos
        if variaveis.algoritmo == 'fifo':
            fifo(LerArquivo(conteudo), variaveis.steps)
        elif variaveis.algoritmo == 'sjf':
            sjf(LerArquivo(conteudo), variaveis.steps)
        elif variaveis.algoritmo == 'rr':
            rr(LerArquivo(conteudo), variaveis.steps, variaveis.tempo)
        elif variaveis.algoritmo == 'garantido':
            garantido(LerArquivo(conteudo), variaveis.steps, variaveis.tempo)
        elif variaveis.algoritmo == 'loteria':
            loteria(LerArquivo(conteudo), variaveis.steps, variaveis.tempo)

            # fecha o arquivo
    # finally:
    #   arq_obj.close()

    return 0


if __name__ == '__main__':
    main()
