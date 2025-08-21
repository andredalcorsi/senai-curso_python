#Escreva um programa que leia o
#Nome, idade e sexo de 4 pessoas. No final mostre:

#A média de idade do grupo
#Qual é o homem mais velho
#Quantas mulheres têm menos de 20 anos

media_idade = 0
idade_mais_velho = 0
quant_menos_20 = 0
nome_mais_velho = ""

for counter in range(0, 4):
    nome = str(input('Informe o nome desejado: '))
    sexo = str(input('Qual é o seu gênero? [M/F]: ')).strip().lower()[0]
    idade = int(input('Informe a idade: '))

    media_idade+=idade

    if (sexo != 'm' and idade < 20):
        quant_menos_20 += 1
    if (sexo == 'm' and idade > idade_mais_velho):
        idade_mais_velho = idade
        nome_mais_velho = nome


print(f'Quantidade de mulheres com menos de 20 anos: {quant_menos_20}\n'
      f'A média de idade do grupo é igual a {media_idade / 4}\n'
      f'O homem mais velho se chama {nome} e tem {idade} anos')