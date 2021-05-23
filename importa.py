import mysql
    (user='root', password='', host='127.0.0.1', database='app')
cursor = conexao.cursor()
# Montando o comando insert com as chaves do dicionário
inserir_contato = ("insert into contatos (nome, telefone, celular) "
"values (%(nome_contato)s, %(telefone)s, %(celular)s)")
# Criando um dicionário com os dados a serem inseridos
contato = {'nome_contato':'Bela Adormecida',
'telefone':'(61)2222-5657',
'celular':'(61)95874-5854'}
cursor.execute(inserir_contato, contato)
conexao.commit()
cursor.close()
conexao.close()