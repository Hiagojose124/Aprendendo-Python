#Desafio 16 - Quebrado um número
#Curso em Vídeo - Python
#Resolução:usa math.trunc para cortar a parte decimal

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, trunc(num)))
