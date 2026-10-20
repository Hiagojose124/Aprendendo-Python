#Desafio 024 - Verificando o nome de uma cidade
#Curso em Video - Python
#Solução: Verifica se a cidade começa com "SANTO"

cid = str('input('Em que cidade você nascel ')).strip()
print(cid[:5].upper() == 'SANTO')
