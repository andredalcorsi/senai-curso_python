#Escreva um programa que peça ao usuário para 
#adivinhar um número entre 1 e 10 
#e continue pedindo até que o usuário acerte o número. 
#E no final, retorne também a quantidade de tentativas necessárias.


import random

contador = 0 
computador = random.randint(1, 10)

while contador != computador: 

    contador = int(input('Adivinhe um número: '))
    computador+=contador
   

    if (computador == contador):
        print(f'Número do computador: {computador} x Meu Número: {contador}. Ganhou!')
    else: 
        print('Perdeu')