#Desafio 018 - seno, cosseno e Tangente
#Curso em video - Python
#Resolução: converte graus radianos e mostra seno, cosseno e tangente

import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
