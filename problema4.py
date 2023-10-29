#Faça um programa que peça 2 numeros inteiros e um numero float. Calcule e mostre.

#O produto do dobro do primeiro com metade do segundo
#a soma do triplo do primeiro com o segundo.
#o terceiro elevado ao cubo.


print('Bem vindo ao problema 4, me ajude a resolver\n')

num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
num3 = float(input('digite um numero com virgurla: '))

resultado_1 = (num1*2) * (num2/2)
print(f'resultado 1: {resultado_1}')

resultado_2 = (3* (num1+num2))
print(f'resultado 2: {resultado_2}')

resultado_3 = ((num3)**3)
print(f'resultado 3: {resultado_3}')


print('obrigado pela ajuda')