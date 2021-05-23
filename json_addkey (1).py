

import json 

from pprint import pprint

with open('algoritmocartoes.json','r',encoding='utf-8') as file:
	# dados = eval(dados.read())
	json_data = json.load(file)



novos_dados = []
for dados in json_data:
	# if not dados['created_at']:
		# print(dados)
		# print(dados['created_at'])
		dados['criadoem_at'] = dados['created_at'].replace(' ','T')+'-03:00'
		novos_dados.append(dados)
		# pprint(dados)
		# print('-'*12)
		# input()


with open('algoritmocartoes_fixed.json','w',encoding='utf-8') as escrever:
	escrever.write(str(novos_dados))

