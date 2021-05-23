import mysql.connector
conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='app')
cursor = conexao.cursor()
remover_contato = ("delete from contatos  where nome = 'Pateta'")
cursor.execute(remover_contato)
conexao.commit()
cursor.close()
conexao.close()