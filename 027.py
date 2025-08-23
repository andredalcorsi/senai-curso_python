#Escreva um programa que leia um número n inteiro qualquer
#e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

#Meu código
numero = int(input('Digite o seu número: '))

contador = 0
primeiro_termo = 0
segundo_termo = 1
proximo_termo = 0

while contador < numero:

    primeiro_termo = segundo_termo
    segundo_termo = proximo_termo
    proximo_termo = primeiro_termo+segundo_termo
    contador += 1
    print(proximo_termo)
"""
#Código do Professor 

n = int(input('Quantos números deseja contar? ")

i = 0 
ant = 1 
atual = 1 

while i < n: 
    if i == 0
        print('0')
    elif i == 1:
        print('1')
    elif i == 2: 
        print('1')
    else: 
        p = anterior + atual
        anterior = atual 
        atual = p 
        print(p)
        i+=1
"""
