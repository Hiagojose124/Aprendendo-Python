#Desafio 10 - Conversor de Reais Dólares
#Curso em video - Python
#Resolução: lê valor em reais mostra quntos dólares pode comprar

real = float(input('Quanto dinheiro você tem na cateira? R$'))
dolar = real / 5.19
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
