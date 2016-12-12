#TESTE 01
"""num = int (input ("Digite um numero: "))

if num > 10:
    print("O numero e' maior que 10")
elif num == 10:
    print("O numero e' igual a 10")
else:
    print("O numero e' menor que 10")"""

###############################################
#TESTE 02
"""num = 21

while True:

    resposta = int(input('Digite um numero: '))

    if resposta == num:
        # inicio do bloco
        print ("Parabens, voce venceu este.")
        print ("Mas nao ganhou nada!")
        break
    elif resposta > num:
        #Segunda parte do bloco "Entao SE"
        print ("O numero eh maior que", resposta)
    else:
        #Terceira parte do bloco(Se Nao)
        print ("O numero eh menor que", resposta)"""

#######################################################

#Loop for
    #TESTE 03
"""for i in range(0,10):
    print (i)"""

    #TESTE 04        
"""for i in range(0,30,5):
    print (i)"""

    #TESTE 05
"""num =  int (input ('Digite um numero:'))

for i in range(num + 1):
    print(i)"""

    #TESTE 06
"""print ("----------------------")   
for x in range(1,11):
    for y in range(1,11):
        print ('%d x %d = %d' %(x,y,x*y))
    print ("----------------------")"""

##########################################################

#PROGRAMA NOTE 'while' 01

"""nota = float (input("Digite uma nota de  0 a 10: "))

while nota < 0 or nota >10:
    print ('ERRO: digite uma nota de 0 a 10, por favor!')
    nota = float (input("Digite uma nota de  0 a 10: "))"""

##########################################################

#PROGRAMA NOTE 'while' 02

nota = float (input("Digite uma nota de  0 a 10: "))

while nota < 0 or nota >10:
    try:
        print ('ERRO: digite uma nota de 0 a 10, por favor!')
        nota = float (input("Digite uma nota de  0 a 10: "))
    except (ValueError, TypeError, TabError):
        print('Eu falei nota (numero)!..')




































    
