#Exercício Conversor de Temperatura
#=======================================
#Crie um programa que ofereça ao usuário um menu com as opções descritas abaixo e com base na escolha do mesmo
#faça a conversão de temperatura relativa a opção indicada:

#1- Celsius para Fahrenheit
#2- Fahrenheit para Celsius
#3- Kelvin para Celsius 
#4- Celsius para Kelvin
#5- Fahrenheit para Kelvin
#6- Kelvin para Fahrenheit
#7- Encerrar o programa

#Em caso de erro por parte do usuario o progrma devera apresentar mensagem de erro informativo

print ('''Lista de Conversores de Temperatura:
1- Celsius para Fahrenheit
2- Fahrenheit para Celsius
3- Kelvin para Celsius 
4- Celsius para Kelvin
5- Fahrenheit para Kelvin
6- Kelvin para Fahrenheit''')

temp = int (input ("Digite o numero do tipo de conversão que deseja: "))

if temp == 1:
    C = float (input ("Digite o valor em Celsius: "))
    F = ((C/5)*9)+32
    print ("O valor em Fahrenheit é %5.2f ºF" %F)
elif temp == 2:
    F = float (input("Digite o valor em Fahrenheit: "))
    C = ((F - 32)/9)*5
    print ("O valor em Celsius %5.2f ºC" %C)
elif temp == 3:
    K = float (input("Digite o valor de Kelvin: "))
    C = K - 273
    print ("O valor em Celsius %5.2f ºC" %C)
elif temp == 4:
    C = float (input ("Digite o valor em Celsius: "))
    K = C + 273
    print ("O valor em Kelvin %5.2f K" %K)
elif temp == 5:
    F = float (input("Digite o valor em Fahrenheit: "))
    K = ((F - 32)/9)*5 + 273
    print ("O valor em Kelvin %5.2f K" %K)
elif temp == 6:
    K = float (input("Digite o valor de Kelvin: "))
    F = 1.8 * (K - 273) + 32
    print ("O valor em Fahrenheit é %5.2f ºF" %F)
else:
    print ("""ERRO: Por favor, digite a numeraçao do tipo de conversao que
deseja de acordo com a lista demonstrada.""")
