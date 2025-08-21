#Escreva um programa que verifique se uma frase é um palíndromo.

#Preciso percorrer a palavra e CONTAR QUANTAS LETRAS ELA TEM

#Preciso contar a quantidade de letras que tem na palavra ou na frase ok

# Preciso ignorar os espaços ok

# Preciso equiparar a frase

"""
#1 forma mais eficiente
frase = str(input('Digite uma palavra: ')).lower().replace(" ", "")

pontos = 0
for contador in range(0, len(frase)):
    if frase[contador] == frase[-i-1]:
        pontos+=1

if pontos == len(frase):
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')

"""

#forma fácil

frase = str(input('Digite uma palavra: ')).lower().replace(" ", "")

if frase == frase[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')