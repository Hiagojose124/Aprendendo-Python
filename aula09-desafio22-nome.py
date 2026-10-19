#Desafio 022 - Analisador de Nomes
#Curso em Video - Python
#Solução: mostra nome em Maiúsculos, minúsculas e contas letras

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisado seu nome...')
print('Seu nome e maiúsculo é {}'.format(nome.upper()))
print('Seu nome e minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa [0], len(separa[0])))
