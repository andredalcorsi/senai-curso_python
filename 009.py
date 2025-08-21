#Crie um programa que leia um nome, e mostre o primeiro e o último nome

nome = str(input('Diga seu nome: '))

posicao = nome.find (' ')
primeiro_nome = nome[0:posicao]
ultima_posicao = nome.rfind(' ')
ultimo_nome = nome[ultima_posicao:]

print(f'{nome}\n' 
      f'Primeiro Nome: {primeiro_nome}\n'
      f'Último nome:{ultimo_nome}')