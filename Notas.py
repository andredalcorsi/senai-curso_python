# Operaçôes Matemáticas
'''
print('Olá Mundo!')
print(56 + 37)
print(90 - 85)
print(128 * 37)
print(900 / 8)
print(8 ** 6) # Pontência


# aspas () simples seleciona uma grande area de comentérios

# Variável Interna

idade = 29 # variavel fixa
nome = 'Danilo Quaresma'

print(f'Seu nome é {nome}, e sua idade é de {idade} anos')


# Variavel Externa

nome = input('Digite seu nome:')
print(f'Seu nome é: {nome}')


# Primeiro desafio

idade1 = int(input ("Digite a primira idade:"))
idade2 = int(input ("Digite a segunda idade:"))

soma_idade = idade1+idade2

print(f'A soma das idades é : {idade1+idade2}') #variavel descartavel
print(f'A soma das idades é: {soma_idade}') # forma de variavel reutilizavel


#strings

senai = 'LuIs eulálio'

#Fatiamento

print(senai[0])
print(senai[3:9])
print(senai[:7])
print(senai[3:])

#Analise
print(len(senai))
print(senai.count('l'))
print(senai.find('l'))
print(senai.rfind('l'))

#Transformação

print(senai.upper())
print(senai.lower())
print(senai.capitalize())

senai_novo = senai.replace('L','S')

nome = input('Digite seu nome').strip()

print(nome)

#For

#1

for i in range(1,10):
    print('*')

#2

for i in range (1, 101):
    print(i)

#3

for i in range (10, 0, -1):
    print(i)

#4

soma = 0

for i in range (1, 11):
n = int(input('N: '))
soma = soma + n

print(soma)

#while

contador = 0

while contador < 5:
    print('Oi')
    contador +=1

    #1

    contador = 0

    while contador < 5:
        print('Oi')
        contador+=1

    #2
    resposta = 'S'

    while resposta != 'N':
        print('?')
        resposta = input('Deseja Continuar? [S/N]: ').strip().upper()[0]


    # while true

    while True:
    n = int(input('Digite algo [999 para parar]: ')

    if n == 999:
        break

    while True:
        opcao = int(input('1. OI'
                          '\n 2. Olá'
                          '\n 3. Bem-Vindo'
                          '\n4. Sair ----> '))
        if opcao == 1:
            print('OI')
        elif opcao == 2:
            print('Olá')
        elif opcao == 4:
            print('Até logo')
            break
'''



