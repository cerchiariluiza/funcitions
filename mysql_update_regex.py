
import mysql.connector
conexao = mysql.connector.connect(user='root', password='', host='localhost', database='coletor_cc')
cursor = conexao.cursor()


visa = ("update temporaria set bank = 'VISA' where bank_name is null and number REGEXP '^4[0-9]{15}$' limit 10")
bandeira = ('VISA')
cursor.execute(visa, bandeira)
conexao.commit()
cursor.close()
conexao.close()