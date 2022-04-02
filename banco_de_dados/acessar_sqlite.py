import sqlite3

"""
 Cria uma conexão com o banco de dados.
 Se o banco de dados não existir, ele é criado neste momento.
"""
con = sqlite3.connect("escola.db")

"""
 Criar um cursor.
 Um cursor permite percorrer todos os registros em um conjunto de dados.   
"""
cur = con.cursor()

# Cria uma instrução sql
sql_create = (
    "create table if not EXISTS cursos "
    "(id integer primary key, "
    "titulo varchar(100), "
    "categoria varchar(100))"
)

# Executando a instrução sql no cursor
cur.execute(sql_create)

# Criando outra sentença SQl para inserir registros
sql_insert = "insert into cursos values (?, ?, ?)"

# Dados
recset = [
    (1000, "Ciência de Dados", "Data Science"),
    (1001, "Big Data Fundamentos", "Big Data"),
    (1002, "Python Fundamentos", "Análise de Dados"),
]

# Inserindo os registros
for rec in recset:
    cur.execute(sql_insert, rec)

# Grava a transação no banco
con.commit()

# Criando outra sentença SQL para selecionar registros
sql_select = "select * from cursos"

# Seleciona todos registros armazenado-os no cursor
cur.execute(sql_select)

# Recupera os resultados
dados = cur.fetchall()

# Mostra
for linha in dados:
    print("Curso Id: %d, Título: %s, Categoria: %s" % linha)

# Gerando outros registros
recset = [
    (1003, "Gestão de Dados com MongoDB", "Big Data"),
    (1004, "R Fundamentos", "Análise de Dados"),
]

# Inserindo os registros
for rec in recset:
    cur.execute(sql_insert, rec)

# Gravando a transação
con.commit()

# Seleciona todos registros armazenando-os no cursor
cur.execute("select * from cursos")

# Recupera os resultados
recset = cur.fetchall()

# Mostra
for rec in recset:
    print("Curso Id: %d, Título: %s, Categoria: %s" % rec)

# Fecha o cursor
cur.close()

# Fecha a conexão
con.close()
