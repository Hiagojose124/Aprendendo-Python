#Desafio 035 - Analisando Triângulo v1.0
#Curso em Video - Python
#Resolução: Verifica-se 3 segmentos podem formar um triângulo

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Os segmentos acima PODEM FORMAR triângulo!')
else:
  print('Os segmento acima NÂO PODEM FORMAR triângulo!')
  
