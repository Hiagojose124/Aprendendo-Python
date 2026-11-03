#Desafio 030 - Par ou ìmpar
#Curso em Video -python
#Solução: Verifica se um número inteiro é PAR ou ÌMPAR

número = int(input('Me diga im número qualquer: '))
resultado = número % 2
if resultado == 0:
  print('O número {} é PAR'.format(número))
else:
  print('O número {} é ÌMPAR'.format(número))
  
