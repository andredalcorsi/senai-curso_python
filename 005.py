#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

raio = float(input('Qual é o raio que você quer informar? '))

calculo_volume = (((4/3) * 3.14) * (raio ** 3))
calculo_area = (((4 * 3.14) * (raio ** 2)))

print(f'Volume da esfera: {calculo_volume}')
print(f'Área da esfera: {calculo_area}')