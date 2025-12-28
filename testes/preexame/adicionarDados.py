import sqlite3

conn = sqlite3.connect("concessionaria.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# cursor.execute("""
# INSERT INTO condutor(nome, telefone) VALUES ("Tiago", "987987987"), ("Davi", "987987987")
# """)

cursor.execute("""
INSERT INTO automovel(modelo, id_condutor) VALUES ("Honda", 1), ("Toyota", 2), ("BMW", 2)
""")



conn.commit()
conn.close()