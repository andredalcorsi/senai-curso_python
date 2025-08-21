#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

idade = int(input('Insira sua idade: '))
peso = float(input('Insira seu peso. Kg: '))
gripe = str(input('Você apresentou sinais de gripe nos últimos dias? [S/N]')).strip.upper()[0]
jejum = float(input('Você está de Jejum a quantas horas? '))
repouso = int(input('Insira a quantidade de horas dormidas: '))
alcool = str(input('Você consumiu álcool nas últimas 12h? [S/N]')).strip().upper()[0]

if idade >= 18 and idade <= 69 and peso >= 50 and gripe == 'N' and jejum >= 3 and repouso >= 6 and alcool >= 'N': 
    print('Apto a doar sangue')
else: 
    print('Volte outro dia')