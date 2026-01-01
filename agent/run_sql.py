import sqlite3

query = input("Enter SQL query: ")

conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
