#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

numero = int(input('Insira um número: '))

if numero % 2 == 0:
    print(f'{numero} é Par.')
else: 
    print(f'{numero} é Ímpar.')
