#Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome


nome = str(input('Diga o seu nome: '))

print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))
print(len(nome[0:nome.find(' ')]))

