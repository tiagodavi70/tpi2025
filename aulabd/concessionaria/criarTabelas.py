import sqlite3

conn = sqlite3.connect("concessionaria_prof.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Condutor (
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    telefone TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Automovel (
    id INTEGER PRIMARY KEY NOT NULL,
    modelo TEXT NOT NULL,
    id_condutor INTEGER,
    FOREIGN KEY (id_condutor) REFERENCES Condutor(id)                       
);
""")

conn.commit()
conn.close()