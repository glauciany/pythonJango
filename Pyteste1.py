#!/usr/bin/env python3

print ('Programa em Linguagem de programaçao Python')

num0 = int (input ('Digite um numero inteiro: '))
num1 = int (input ('Digite um numero inteiro: '))
nome = input ('Digite seu nome: ')
soma = num0 + num1

print (nome + ' voce digitou ', num0 , num1)
print ('A soma dos numeros e: ', soma)

if soma % 2 == 0:
    print ('O resultado retornado e "PAR"')

else:
    print ('O resultado retornado e "IMPAR"')



