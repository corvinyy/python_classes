'''database = 'nome_database.db'
conexao = sqlite3.connect(database)
cursor = conexao.cursor()'''

import sqlite3

database = 'livraria.db'
conexao = sqlite3.connect(database)
curs = conexao.cursor()

'''sql = create table tb_cliente (
    cpf text primary key,
    nome text not null,
    idade integer)'''

sql = '''create table if not exists tb_cliente (
    cpf text primary key,
    nome text not null, 
    idade integer)'''

curs.execute(sql)
curs.close()
conexao.close()
print("Fechou a base de dados")

