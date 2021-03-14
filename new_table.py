import sqlite3

connection = sqlite3.connect("data.db") 
#use whatever name you want, just finish with .db
#O comando connect() do sqlite3 cria o arquivo do banco de dados 

connection.execute ("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER NOT NULL)")

#O comando execute() da conexão te permite executar qualquer comando SQL que quiser no seu banco de dados, basta escrever como uma string com ele dentro, também dá pra colocar parâmetros nela, veremos como depois.

print ("Your table has been created")