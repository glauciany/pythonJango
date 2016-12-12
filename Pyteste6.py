###############Aula Py - 02/12/2016 #######################

#TESTE 01

'''import random

for i in range(10):
    x = random.random()
    print (x)'''
    
#######################################################
#TESTE 02

'''import random

num = random.randint(0,10)

print(num)

while True:
    nun1 = random.randint(0,10)
    print(nun1)
    
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
        print ("O numero eh menor que", resposta)'''

###################################################################
#TESTE 03

'''fruta = 'uva','maça'

for letra in fruta:
    print(letra)'''

#####################################################################
#TESTE 04

'''tup = ('a','l','u','n','o')

unir = ''.join(tup)

print(unir)'''

#######################################################################
#TESTE 05

'''carroCor = {}
carroCor['Fusca'] = 'preto'
carroCor['Palio'] = 'vermelho'

carroAno = {}
carroAno['Opala'] = 1977
carroAno['Uno'] = 2010

print(carroCor)
print (carroAno)'''

########################################################################
#TESTE 06

dict = {'Fusca':'preto','Opala':1977}

'''print(dict ['Fusca'])
print(dict ['Opala'])

print ('Fusca: ',dict ['Fusca'],'/','Opala: ',dict ['Opala'])

for k in dict:
    print (k , dict[k])

for k in sorted(dict):
    print (k+':',dict[k])'''

#########################################################################
                ###EXERCICIO###


nome = str(input('Digite o nome: '))
idade = int(input('Digite o idade: '))
telefone = int(input('Digite o telefone: '))
endereço = str(input('Digite o endereço: '))

dadosPessoais = {"nome":nome , 'idade': idade, telefone:'', endereço:''}

for d in sorted(dadosPessoais):
    print (d ,dict[dadosPessoais])


    



































