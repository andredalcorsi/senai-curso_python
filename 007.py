#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.

salario = float(input('Valor do salário: '))

reajuste = salario * (60/100)

print(f'Salário inicial: {salario}. Salário com reajuste: {reajuste+salario}')