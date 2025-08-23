#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

#1.	Somar
#2.	Multiplicar
#3.	Maior
#4.	Novos números
#5.	Sair do programa


n1 = 0
n2 = 0
n3 = 0

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

while True:

    soma = n1+n2+n3
    mult = n1*n2*n3
    novos_numeros = n1+n2+n3

    escolha = int(input('Qual opção você deseja escolher?\n'
                        '[01 - SOMAR]\n'
                        '[02 - MULTIPLICAR]\n'
                        '[03 - MAIOR]\n'
                        '[04 - NOVOS NÚMEROS]\n'
                        '[05 - SAIR DO PROGRAMA]'))
    if escolha == 1:
        print(f'A soma dos valores {n1}, {n2} e {n3} é igual a {soma}')
    elif escolha == 2:
        print(f'O resultado da multiplicação dos valores {n1}, {n2} e {n3} é igual a {mult} ')
    elif escolha == 3:
        if (n1 > n2):
            print(f'O maior número entre os valores {n1}, {n2} e {n3} é igual a {n1}')
        elif (n2 > n3):
            print(f'O maior número entre os valores {n1}, {n2} e {n3} é igual a {n2}')
        elif (n3 > n1):
            print(f'O maior número entre os valores {n1}, {n2} e {n3} é igual a {n3}')

    elif escolha == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        n3 = int(input('Digite o terceiro número: '))

    elif escolha == 5:
        break






