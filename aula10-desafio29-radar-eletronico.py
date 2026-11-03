#Desafio 029 - Radar Eletrônico
#Curso em Video - Python
#Solução: Verifica se o carro ultrapassou o limite de 80km/h e calcula a multa 

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
  print('MULTADO! Você  excedeu o limite permitido que é de 80km/h')
  multa = (velocidade-80) * 7
  print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
