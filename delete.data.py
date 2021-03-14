import sqlite3

connection = sqlite3.connect("data.db")

connection.execute("DELETE FROM users")

#conexao.execute("DELETE FROM usuarios WHERE id=?", [3])
#To delete one specific query of the table
connection.commit()

print("Your monsters, you have deleted everything!")