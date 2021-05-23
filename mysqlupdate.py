
# import mysql
# import mysql.connector
import mysql.connector as mysql
conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='app')
cursor = conexao.cursor()
atualizar_contato = ("update contatos set nome = %s, telefone = %s, celular = %s where nome= 'Pocahontas'")
contato = ('Pocahontas', '(28)6888-8888', '(28)88888-8888')
cursor.execute(atualizar_contato, contato)
conexao.commit()
cursor.close()
conexao.close()