import sqlite3

conexao = sqlite3.connect('livraria.db')
curs = conexao.cursor()

sql = '''insert into tb_cliente  
    (cpf, nome, idade)
    values('372656401','Rafael', 18)'''


curs.execute(sql)
conexao.commit()
curs.close()
conexao.close()
print("Fechou a base de dados")
