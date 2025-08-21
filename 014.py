#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

letra = str(input('Digite uma letra: '))

vogais = ['a', 'e', 'i', 'o', 'u']

if (letra in vogais):
    print('Vogal')
else: 
    print('Consoante')