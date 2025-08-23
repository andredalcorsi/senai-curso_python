#Crie um programa que leia vários números inteiros.
#O programa só vai parar quando o usuário digitar 0000.
#No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)


contador = 0
soma = 0

while True:

    n = int(input('Digite um número: '))
    contador+=1

    soma = n + soma

    if n == 0000:
        break



print(f'Quantidade de números digitados: {contador-1}\n'
      f'A soma entre os números digitados é igual a {soma}')

