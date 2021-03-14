import sqlite3

connection = sqlite3.connect("data.db")
#Esse comando cria um cursor, um objeto que usamos para executar comandos SQL, mas que salva qualquer dado que retornar a partir desses comandos, sempre que usar um SELECT, use um cursor 

cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
#Esse comando execute um comando SQL usando o cursor

#cursor.execute("SELECT * FROM users WHERE id=?", [1]) 
#Searching info using a list

resultados = cursor.fetchall()
#Esse comando retorna os resultados dos comandos cursor.execute() anteriores para que possamos os usar diretamente ou os salvar em uma variavel, como fizemos nesse caso

print ("Resultados:")
for usuario in resultados:
    print(usuario)