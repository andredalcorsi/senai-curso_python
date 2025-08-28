#Crie um programa que leia vários números inteiros.
#O programa só vai parar quando o usuário digitar 0000.
#No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)


contador = 0
soma = 0

while True:

    n = input('Digite um número: ')
    if n == '0000':
        break

    soma += int(n)

    contador += 1


print(f'Quantidade de números digitados: {contador}\n'
      f'A soma entre os números digitados é igual a {soma}')

