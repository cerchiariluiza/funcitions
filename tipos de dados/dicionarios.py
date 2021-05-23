dados_cliente = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}

# print(dados_cliente) # {'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul', 'Telefone': '982503645'}

dados_cliente.pop('Telefone', None)
del dados_cliente['Nome']

print(dados_cliente)