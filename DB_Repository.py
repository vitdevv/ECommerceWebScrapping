import sqlite3

conexao = sqlite3.connect('clientes.db')

c = conexao.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS ProductPrice
(
    pdID INTEGER PRIMARY KEY AUTOINCREMENT
    ,pdName text
    ,pdPrice float
    ,pdDate date
)      
''')

conexao.commit()
conexao.close()
