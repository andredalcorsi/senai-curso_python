#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000,00
#Qual é o produto mais barato

nome_prod = ""
total_compra = 0
contador = 0
mais_mil = 0
mais_barato = 0

while True:

    nome_prod = input('Digite o nome do produto: ')
    preco_prod = float(input('Digite o preço do produto: '))

    total_compra+=preco_prod

    if preco_prod >= 1000:
        mais_mil+=1
    
    if contador == 0 or preco_prod < mais_barato: 
        mais_barato = preco_prod
        
    contador+=1
    
    print(f'Total Gasto na Compra: {total_compra}')
    print(f'Quantos produtos custam mais de mil reias: {mais_mil}')
    print(f'Produto mais barato: {mais_barato}')