#Desafio 034 - Aumento Salarial
#Curso em Video - Python
#Resolução: Pergunta o salário e calcula o valor do aumento

salario = float(input('Qual é o salário do funcionário R$'))
if salario <= 1250:
  novo = salario + (salario * 15 / 100)
else:
  novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))
