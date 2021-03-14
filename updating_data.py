import sqlite3

connection = sqlite3.connect("data.db")

#connection.execute ("UPDATE users SET name='Something Awesome'")
#Changing everything


connection.execute("UPDATE users SET age=? WHERE id=?", [28, 2])
#Changing specific information


connection.commit()

print("You have fucked everything")