import sqlite3

conn = sqlite3.connect("clinica.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO paciente(nome) VALUES ("Pedro"), ("João"), ("Alexandre"), ("Bernardo"), ("Bruno")
""")

cursor.execute("""
INSERT INTO medico(nome, especialidade) VALUES 
 ('Pedro', 'Pediatria'),
 ('João', 'Pediatria'),
 ('Rodrigo', 'Dentista'),
 ('Maria', 'Cardiologia'),
 ('Isabel', 'Oncologia')
""")

cursor.execute("""
INSERT INTO consulta(data, paciente_id, medico_id) VALUES
 ("2025-12-29", 1, 1),
 ("2025-12-29", 2, 2),
 ("2025-12-29", 3, 3)
""")

cursor.execute("""
INSERT INTO exame(nome, id_consulta) VALUES
 ("Raio X", 5),
 ("Raio X", 6),
 ("Raio X", 7)
""")

conn.commit()
conn.close()
