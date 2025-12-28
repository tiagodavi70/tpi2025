import sqlite3

conn = sqlite3.connect("exame.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS medico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especialidade TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS paciente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(45) NOT NULL
);
""")

cursor.execute("""         
INSERT INTO paciente (nome) VALUES
('Tiago Araújo'),
('Izabella Silva'),
('Karla Alves'),
('Bruno Costa'),
('Eduarda Betin');
""")

cursor.execute("""         
CREATE TABLE IF NOT EXISTS consulta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE NOT NULL,
    paciente_id INTEGER NOT NULL,
    medico_id INTEGER NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES paciente(id),
    FOREIGN KEY (medico_id) REFERENCES medico(id)
);             
""")

cursor.execute("""
INSERT INTO medico (nome, especialidade) VALUES
('João Pereira', 'Cardiologia'),
('Maria Santos', 'Pediatria'),
('Carlos Lima', 'Ortopedia'),
('Paula Ribeiro', 'Cardiologia'),
('Ricardo Alves', 'Neurologia');
""")

cursor.execute("""
INSERT INTO consulta (data, paciente_id, medico_id) VALUES
('2025-01-10', 1, 1),
('2025-01-11', 2, 2),
('2025-01-12', 3, 3),
('2025-01-13', 4, 4),
('2025-01-14', 5, 5);
""")

conn.commit()
conn.close()
