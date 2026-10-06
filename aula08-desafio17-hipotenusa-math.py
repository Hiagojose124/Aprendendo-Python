#Desafio 17 - Catetos e  Hipotenusa
#Curso em video - Python
#Resolução:usa math.hypot para calcular automaticamente

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

