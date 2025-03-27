import sqlite3

#sql = '''select (* | nome_coluna1 [, nome_coluna2, ...]) 
        #from nome_tabela
        #[where ...]'''

conexao = sqlite3.connect('livraria.db')
curs = conexao.cursor()

sql = 'select * from tb_cliente'
curs.execute(sql)

l_registros = curs.fetchall()
print(l_registros)

curs.close()
conexao.close()
print("Fechou a base de dados")
