#Desafio 004 - Descobrindo o tipo e informações de um valor
#Curso em Vídeo - Python
#Resolução: lê um valor e mostra seu tipo e todas as informação possíveis

a=input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('So tem espaços?', a.isspace())
print('È um número?', a.isnumeric())
print('È alfabético?', a.isalpha())
print('È alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())
