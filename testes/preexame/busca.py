import sqlite3

conn = sqlite3.connect("concessionaria.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
SELECT nome, telefone FROM condutor
""")

cursor.execute("""
SELECT * FROM automovel
""")

cursor.execute("""
SELECT * FROM condutor WHERE nome = 'Tiago'
""")

cursor.execute("""
SELECT automovel.id, modelo, nome, telefone FROM condutor, automovel WHERE id_condutor == condutor.id
""")

linhas = cursor.fetchall()
print(linhas)

conn.commit()
conn.close()