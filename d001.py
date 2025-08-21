# Escreva um programa que execute o cálculo da Função horária da posição no MRUV
# Retorne de acordo com o tempo informado pelo usuário

tempo = float(input('Insira o tempo desejado: '))
space_init = float(input('Insira o espaço desejado: '))
vel_init = float(input('Insira a velocidade inicial: '))
aceleracao = float(input('Insira a aceleração: '))

sorvetao = float(space_init + vel_init * tempo + (aceleracao*(tempo**2))/2)

print(f'A posição do objeto no tempo {tempo} é de {sorvetao} (m)')