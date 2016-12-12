#dict1 = {"Nome":"Jose", "Sexo":"Masculino","Cidade":"Teresina"}
#dict2 = {"Nome":"Maria", "Sexo":"Feminino","Cidade":"Teresina"}


#print(dict1,dict2)


'''cmp(dict1,dict2) ===> Compara elementos entre dicionarios

len(dict1) ===> Retorna o comprimento entre dicionario

str(dict2) ===> Retorna como texto o dicionario

type(dict1) ===> mostra a que classe pertence o dicionario

dict1.clear() ===> Apaga o conteudo do dicionario

dict1.copy() ===> Faz uma copia do dicionario

dict1.update(dict2) ===> Acrescenta algum elemento em um dicionario ou pode
                         subsitituir os elementos de um dicionario para outro

dict.fromkeys() ===> cria um novo dicionário com chaves de seq e
                     valores definidos como value

dict.get(key, defaut t=None) ===> retorna um valor para a chave dada.
                                  Se a chave não estiver disponível,
                                  retorna o valor padrão Nenhum.

dict. items() ===> etorna uma lista de dítu (chave, valor) tupla pares

dict.keys() ===> retorna uma lista de todas as chaves disponíveis no dicionário.

dict.values() ===> retorna uma lista de todos os valores disponíveis em um
                   determinado dicionário.

dict.setdefault(key, default=None) ===> Mas irá definir dict [key] = Padrão
                                        se a chave ainda não estiver em dict.

k in dict ===> 

k not in dict ===> 

del dict [key] ===> 

dict.pop(key) ===> 

dict.popitem() ===>

'''
######################################################
'''agenda = {}

agenda ['Raimundo Nonato'] = '(88) 99550-1234'
agenda ['Jose da Silva'] = '(88) 98999-4321'
agenda ['Maria de Jesus'] = '(86) 99999-7410'
agenda ['Bruna Silveira'] = '(99) 98888-0369'

agenda.items()

agenda.keys()

agenda.values()

for k, v in agenda.items():
	print(k, v)'''

###########################################################




















































