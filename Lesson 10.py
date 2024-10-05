import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()


#cur.execute("CREATE TABLE USERS (name TEXT);")


user = input("Username: ")
cur.execute(f"INSERT INTO USERS (name) VALUES ('{user}', '{}');")

connection.commit()

connection.close()