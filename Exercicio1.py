"""Exercicio com execuçao condicional"""

#Escreva um programa que solicite do usuario uma entrada de numero, teste se o mesmo e positivo ou negativo
#e escreva o resultado na tela.

print ('Programa para saber se o numero e positivo ou negativo')

num = float (input ('Digite o numero: '))
if num <= 0:
    print (num," Numero positivo")
else:
    print (num, " Numero negativo")


