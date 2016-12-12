'''for caracter in texto:
      if caracter in 'aeiou':
         vogais = vogais + 1
    else:
         consoantes = consoantes + 1
          
  print "Vogais: %d" %vogais
  print "Consoantes: %d" %consoantes
  print "Total de letras: %d - %d" %(len(texto)'''

# --------- Fim programa ------------

# -------------------------
# EXERCÍCIOS VALENDO PONTOS
# -------------------------

'''
Só para lembrar: Exercícios copiados não valem pontos
-----------------------------------------------------

1. – Escreva um programa que conte a quantidade de vogais em um texto,
     considere criar uma função para tanto.'''

frase = (str(input('Digite uma frase: ')))
def contvogais(frase):
    vogais = 'aeiou'
    nvogais = 0
    for texto in frase:
        if texto in vogais:
            nvogais += 1
    return (nvogais)
print(contvogais (frase))


'''2. - Melhore o programa criando do item 1. para que conte as vogais do
     texto independente de estarem em maiúsculas ou minúsculas.'''

frase = (str(input('Digite uma frase: ')))
def contvogais(frase):
    vogais = 'a','e','i','o','u','A','E','I','O','U'
    nvogais = 0
    for texto in frase:
        if texto in vogais:
            nvogais = nvogais + 1
    return (nvogais)
print(contvogais (frase))

'''3. – Melhore o programa do item 2. para que armazene a quantidade de vogais
     como chave e o texto como valor em um dicionário.
'''



  













