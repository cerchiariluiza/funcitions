
import mysql.connector
conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='app')
cursor = conexao.cursor()

consulta = ("select nome, telefone, celular from contatos where nome like 'M%'")
cursor.execute(consulta)
a = {}
for (nome, telefone, celular) in cursor:
    print(f"Nome: {nome}, telefone: {telefone}, celular: {celular}")
    a = {[f"Nome: {nome}, telefone: {telefone}, celular: {celular}"]}
cursor.close()
conexao.close()