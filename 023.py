#Escreva um programa que leia o peso de 7 pessoas,
# e no final, mostre qual foi o maior e o menor peso lidos
"""
maior = 0
menor = 1000

for contador in range(0, 7):
    peso = float(input('Digite o seu peso: '))

    if (peso > maior):
        maior = peso

    if (peso < menor):
        menor = peso


print(f'Mais pesado: {maior}\n'
      f'Mais leve: {menor}')

"""

maior= None
menor = None

for i in range(7):
    peso = float(input('Peso: '))

    if menor == None and maior == None:
        menor = peso
        maior = peso

        if (peso > maior):
            maior = peso

        if (peso < menor):
            menor = peso

print(f'Mais pesado: {maior}\n'
      f'Mais leve: {menor}')