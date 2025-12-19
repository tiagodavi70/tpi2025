import sqlite3

conn = sqlite3.connect("cliente.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE Cliente(
 id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT,
 telefone TEXT
);

""")

conn.commit()
conn.close()