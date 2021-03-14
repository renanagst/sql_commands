import sqlite3

connection = sqlite3.connect("data.db")

connection.execute("INSERT INTO users (name, age) VALUES('John', 25)")
connection.execute("INSERT INTO users (name, age) VALUES('Linda', 24)")
connection.execute("INSERT INTO users (name, age) VALUES('Sam', 23)")
connection.commit()
#o conexao.commit() que salva as alterações que fizemos no banco de dados.

print("Congratualion, You have create 3 new users.")