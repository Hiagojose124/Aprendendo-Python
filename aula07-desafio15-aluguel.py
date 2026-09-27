#Desafio 15 - Aluguel de carros
#Curso em video - Python
#Resolução:calcula valor a pagar por dias e km rodado

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
