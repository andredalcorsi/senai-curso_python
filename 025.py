#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10
#e continue pedindo até que o usuário acerte o número.
#E no final, retorne também a quantidade de tentativas necessárias.

import random

contador = 0
meu_numero = int(input('Digite um número: '))

aleatorio = random.randint(0,10)

while aleatorio != meu_numero:

    print(f'Não é este número. Tentativa de nº{contador+1}')
    contador+=1

    meu_numero = int(input('Digite um número: '))

    if meu_numero == aleatorio:
        print(f'Acertou! Tentativa de nº{contador}')