#Desafio 12 - Calculando Desconto 
#Curso em video - Python
#Resolução: lê preço e mostra valor com 5% de desconto

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
