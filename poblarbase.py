import sqlite3

# Me conecto a la base de datos o la creo si no existe.
conn = sqlite3.connect('database.db')

# Genero un cursor que voy a utilizar para apuntar a los elementos de la base de datos.
c = conn.cursor()

# Inserto data a la tabla
c.execute("""INSERT INTO proveedores VALUES (
        'James',
        'Doe',
        'jdoe@abb.com',
        'ABB Mexico',
        'Mexico',
        'Motores')""")

# Guardo lo que modifique.
conn.commit()

# Cierro la conexion.
conn.close()
