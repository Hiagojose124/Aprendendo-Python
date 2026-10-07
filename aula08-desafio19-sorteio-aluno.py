#Desafio 019 - Sorteando um aluno
#Curso em video - Python
#Resolução: sorteia 1 aluno dentre 4

from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.fromat(escolhido))
