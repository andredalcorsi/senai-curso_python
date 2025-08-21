# Crie um programa que leia uma frase e mostre:

# Quantas vezes aparece a letra “a”
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece na última vez

frase = str(input('Digite uma frase: ')).strip.lower()

frase = frase.replace('á', 'a')
frase = frase.replace('â', 'a')
frase = frase.replace('ã', 'a')
frase = frase.replace('à', 'a')

print(f'Quantidade de A: {frase.count('a')}')
print(f'Primeiro A:{frase.find('a') +1}')
print(f'Último A: {frase.rfind('a')}')
