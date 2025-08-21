#Crie um programa para jogar JOKEMPO, usando a função random.randint

#Importing the lib. It'll make my script work as expected
import random

#Setting the variable names to choose between rock, paper or scissor
pedra = 0
papel = 1
tesoura = 2

#Setting the variables 
computador = random.randint(0, 2)
escolha = int(input('Digite sua jogada (0 - Pedra | 1 - Papel | 2 - Tesoura): '))

#Changing numbers to string
computador_str = str(computador).replace('0', 'pedra').replace('1', 'papel').replace('2', 'tesoura').upper()
escolha_str = str(escolha).replace('0', 'pedra').replace('1', 'papel').replace('2', 'tesoura').upper()

#Showing the results on screen as I settled up 
print (f'Computador escolheu: {computador_str}!')
print(f'Você escolheu: {escolha_str}!')

#Applying the if condition to make the program work as I want
if (escolha == computador):
    print('Empate')
elif (escolha == papel and computador == pedra) or (escolha == pedra and computador == tesoura) or (escolha == tesoura and computador == papel):
    print('Venceu')
else:
    print('Perdeu')