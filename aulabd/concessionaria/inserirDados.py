import sqlite3

conn = sqlite3.connect("concessionaria_prof.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# EXECUTA E COMENTA
# cursor.execute("INSERT INTO Condutor(nome, telefone) VALUES ('Tiago', '987987987')")
# cursor.execute("INSERT INTO Condutor(nome, telefone) VALUES ('João', '987987988')")
# cursor.execute("INSERT INTO Condutor(nome, telefone) VALUES ('Alexandre', '987987989')")

# cursor.execute("INSERT INTO Automovel(modelo, id_condutor) VALUES ('Honda Civic', 4)")


conn.commit()
conn.close()