#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000

contador = 0

while True:

    tabuada_str = input('Você quer que eu faça a tabuada do: ')

    if tabuada_str == '0000':
        print('Programa encerrado!')
        break
    
    tabuada = int(tabuada_str)

    for contador in range(1,11): 
        print(f'{tabuada}x{contador} = {tabuada*contador}')
    contador+=1
