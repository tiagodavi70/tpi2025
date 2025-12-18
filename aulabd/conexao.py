import sqlite3

conn = sqlite3.connect("cliente.db")
conn.execute("PRAGMA foreign_keys = ON")

cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Cliente (
#     id_cliente INTEGER PRIMARY KEY,
#     nome TEXT NOT NULL,
#     telefone TEXT
# )
# """)


cursor.execute(
    "INSERT INTO Cliente(nome, telefone) VALUES ('Tiago Araújo', '99999-0000')"
)

cursor.execute(
    "INSERT INTO Cliente(nome, telefone) VALUES (?, ?)",
    ("João Silva", "99999-1111")
)

clientes = [
    ("Maria Souza", "98888-2222"),
    ("Carlos Pereira", "97777-3333"),
    ("Ana Lima", "96666-4444"),
    ("Pedro Santos", "95555-5555"),
    ("Lucas Rocha", "94444-6666"),
]

cursor.executemany(
    "INSERT INTO Cliente (nome, telefone) VALUES (?, ?)",
    clientes
)

conn.commit()

conn.close()