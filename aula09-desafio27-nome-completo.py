#Desafio 027 - Primeiro e Último Nome 
#Curso em Video  - Python
#Solução: mostra o primeiro e o último nome de uma pessoa

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1))
