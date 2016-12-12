#Iterando lista
#--------------
#'''Dada uma lista de valores, fornecida abaixo, escreva um programa para encontrar
#o maior valor sequenciadoda esqueda para direita. O programa devera escrever
#a cada loop o valor atual da lista e qual o maior ate aquele momento.'''

"""maior = 0
lista = [1,9,41,12,3,74,15,0]

print("Antes", maior)
for n in lista:
   if n > maior:
      maior = n
   print(maior, n)  
print ("Depois", maior)"""

######################################################################################

"""Escreva um programa que solicite ao usuario que digite
algo no terminal e como saida o programa escrevara a
informaçao relativa ao cumprimento da String digitada.

Para sair encerrar o programa o usuario devera escrever a palavra 'sair'."""

###Teste
'''num = 0
while (num < 9):
   print ("numero:", num)
   num = num + 1
print ('Tchau')'''

x = str (input ('Digite uma palavra: '))
while x <= 10:
   print (len(x))
   x = len (x)
print ('Chega!')
