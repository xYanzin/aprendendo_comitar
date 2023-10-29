#Loja de tintas
#o programa devera pedir o tamanho em metros quadrados da area a ser pintada.
#considere que a cobertura de tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
#em latas de 18 litros que custam 80 reais
#Informe ao usuario a quantidade de latas de tinta a ser comprada e o preço total.

print('Bem vindo a Loja de tintas YCSS\n')
print('Estou aqui para te auxiliar na compra de tintas para sua residencia.\n')

tamanho_a_ser_pintado = int(input('Por gentileza, insira a quantidade de metros quadrados que gostaria de pintar?'))

print(f'Certo!, Você gostaria de pintar {tamanho_a_ser_pintado} de metros')

Resultado_Litros = (tamanho_a_ser_pintado / 3)
Resultado_latas = (Resultado_Litros / 18)
Resultado_Valor = (Resultado_latas * 80)

#def round(Resultado_Litros 3 )       estou tentando limitar em apenas 3 casas
#def round(Resultado_latas 3)         mas ainda nao consegui
#def round(Resultado_Valor 3)

print(f'Você precisarar comprar {Resultado_latas} latas, que lhe custarão {Resultado_Valor}')