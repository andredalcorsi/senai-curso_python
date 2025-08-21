#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.

numero_01 = int(input('Insira um número: '))
numero_02 = int(input('Insira outro número: '))

if (numero_01 == numero_02): 
    print(f'{numero_01} e {numero_02} são iguais.')
else: 
    print(f'Os números {numero_01} e {numero_02} são diferentes.')