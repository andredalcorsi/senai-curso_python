#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

numero = float(input('Digite um número: '))

if numero > 0: 
    print(f'{numero} é positivo.')
elif numero == 0:
    print('Neutro')
else: 
    print(f'{numero} é negativo.')