# Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder. Ao final deve mostrar a quantidade de vitórias

import random

pc = random.randint(1,10)

vitorias = 0

while True:
    print('-------------------------------------------------------------')
    escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()[0]
    j = int(input('Digite um número entre 1 e 10: '))


    while j < 1 or j > 10:

        j = int(input('Digite um número entre 1 e 10: '))

    if ((pc + j) % 2 == 0 and escolha == 'P') or ((pc + j) % 2 != 0 and escolha == 'I'):
        print(f'Vitória - Soma = {pc + j}')
        vitorias+=1
    else:
        print(f'Perdeu com {vitorias} vitórias')
        break