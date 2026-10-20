#Desafio 026 - Primeira e última ocorrência de uma string
#Curso em Video - Python
#Solução: conta e mostra posições de letra 'A' em uma frase


frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
