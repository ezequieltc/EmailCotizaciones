import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""CREATE TABLE proveedores(
    nombre text,
    apellido text,
    email text,
    empresa text,
    pais text,
    destinatarios text
)""")

conn.commit()
conn.close()
