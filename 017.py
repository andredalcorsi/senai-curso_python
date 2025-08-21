#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

peso = float(input('Digite seu peso. Kg: '))
altura = float(input('Digite sua altura. Kg: '))

imc = peso / (altura*altura)

if (imc < 18.5):
    print(f'Seu IMC é {imc}. Você está abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC é {imc}. Você está no Peso Normal')
elif imc >= 25 and imc <= 29.9:
    print(f'Seu IMC é {imc}. Você está em Sobrepeso')
elif imc >= 30 and imc <= 34.9: 
    print(f'Seu IMC é {imc}. Você está em Obesidade Grau I')
elif imc >= 35 and imc <= 39.9: 
    print(f'Seu IMC é {imc}. Você está em Obesidade Grau II')
else:
    print(f'Seu IMC é {imc}. Você está em Obesidade Grau III')