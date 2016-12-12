######Assunto: Arquivos##################

    #### Exmplo 01 ####

###Imprime o resultado do program na tela do terminal.

'''import random

def numsAleatorios(qtdNums):
    for i in range(qtdNums):
        print(random.randint(0,100))

numsAleatorios(11)'''

    #### Exemplo 02 ####

###Gravando o resultado do programa em um arquivo.

'''import random

def numsRnds(qtdNums, arquivo):
    arquivoNums = open(arquivo, 'w')
    for i in range(qtdNums):
        arquivoNums.write(str(random.randint(0,100)))
        arquivoNums.write("\n")

    arquivoNums.close()

numsRnds(100, 'aleatorios.txt')'''

'''import random
def numsRnds(qtdNums, arquivo):
    arquivoNums = open(arquivo, 'w')
    for i in range(qtdNums):
        arquivoNums.write(str(random.randint(0,4)))
        arquivoNums.write("\n")

    arquivoNums.close()

numsRnds(4, 'aleatorios1.txt')'''

    #### Exemplo 03 ####

### Lendo

'''import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

def mediaNums(qtdNums):
    soma = 0
    for i in range(qtdNums):
        num = eval(input('Digite um inteiro: '))
        soma += num
    return soma/qtdNums

print(mediaNums(4, 'aleatorios.txt'))'''

    #### Exemplo 04 ####

'''import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
'''------------------------------------------------'''
def mediaNums(qtdNums, nomeArquivo):
    arquivoNums = open(nomeArquivo)
    soma = 0
    for i in range(qtdNums):
        num = float(arquivoNums.readline().strip())
        soma = soma + num
    arquivoNums.close()
    return soma/qtdNums

print(mediaNums(4, 'aleatorios1.txt'))'''

    #### Exemplo 05 ####

def copiaArquivo(velhoArquivo, novoArquivo):
    arquivo1 = open(velhoArquivo, "r")
    arquivo2 = open(novoArquivo, "w")
    for texto in arquivo1:
        arquivo2.write(texto)

    arquivo1.close()
    arquivo2.close()

copiaArquivo("aleatorios1.txt","novoAleatorios.txt")




















