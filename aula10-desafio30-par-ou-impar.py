#Desafio 030 - Par ou ìmpar
#Curso em Video -python
#Solução: Verifica se um número inteiro é PAR ou ÌMPAR

numero = int(input('Me diga im numero qualquer: '))
resultado = numero % 2
if resultado == 0:
  print('O numero {} é PAR'.format(numero))
else:
  print('O numero {} é ÌMPAR'.format(numero))
  
