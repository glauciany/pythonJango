#Exemplo de nomes para variáveis
#horas_TB = 35
#valor_H = 12.50
#valor_T = horas_TB * valor_H
#print ('O valor do pagamento sera de R$ ',valor_T)


#Funçao para limpar tela (Funçao CLS)

"""A instruçao abaixo faz a importaçao do modulo 'os' """
import os

"""Criando a definiçao da funçao CLS"""
def cls ():
        os.system('cls' if os.name == 'nt' else 'clear')
        
"""Na linha abaixo a chamada da funçao cls()"""
cls()

