#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

tabuada = int(input('Você quer que eu faça a tabuada do: '))

for contador in range(1,11): 
    print(f'{tabuada}x{contador} = {tabuada*contador}')