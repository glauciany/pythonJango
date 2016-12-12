"""Exercicio com execuçao condicional em cadeia"""

#Escreva um programa que solicite do usuario a entrada de dois numeros,
#analise qual dos dois numeros e maior, e em seguida escreva o resultado na tela.

print ('Programa para descobrir qual o maior numero')

num1 = float (input ('Digite o 1º numero: '))
num2 = float (input ('Digite o 2º numero: '))

if num1 > num2:
    print (num1," > ", num2)
elif num1 == num2:
    print (num1," = ", num2)
else:
    print (num1," < ", num2)
