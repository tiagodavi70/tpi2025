import sqlite3

conn = sqlite3.connect("clinica.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM paciente
""")
linhas = cursor.fetchall()
print(linhas)

cursor.execute("""
SELECT * FROM medico WHERE especialidade == 'Cardiologia'
""")
linhas = cursor.fetchall()
print(linhas)

conn.commit()
conn.close()
