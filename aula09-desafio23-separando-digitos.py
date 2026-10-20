#Desafio 023 - Separando Dígotos de um Número 
#Curso em Video - Python
#Solução: lê um número e mostra unidade, dezena, centena e milhar

num = int(input('informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisado o número {}'.format(num)
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
      
