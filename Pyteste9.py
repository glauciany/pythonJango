######### Exemplo 01 ##########

'''import pickle

### Abre um arquivo.dat para escrita em modo binario
arquivo = open('arquivo.dat','wb')
### A funcao dump do modulo pickle escreve o escreve
### O valor fluante 32.3 em arquivo.dat
pickle.dump(32.3, arquivo)  
pickle.dump([12, 15, 18], arquivo)
### Fecha o arquivo.dat
arquivo.close()'''

######### Exemplo 02 ##########

import pickle

arquivo = open('arquivo.dat','rb')
res1 = pickle.load(arquivo)  
res2 = pickle.load(arquivo)

print ('Resultado 1 (float)', res1)
print (type(res1))

print ('Resultado 2 (float)', res2)
print (type(res2))
