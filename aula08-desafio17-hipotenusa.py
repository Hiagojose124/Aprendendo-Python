#Desafio 17 - Catetos e  Hipotenusa
#Curso em video - Python
#Resolução: calcula hipotenusa pela fórmula matemática

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.fromat(hi))
