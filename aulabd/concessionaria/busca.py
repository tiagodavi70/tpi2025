import sqlite3

conn = sqlite3.connect("concessionaria_prof.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Condutor")

linhas = cursor.fetchall()

print(linhas)

conn.commit()
conn.close()