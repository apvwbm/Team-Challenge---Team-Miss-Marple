import sqlite3

# Conexión a SQLite
conn = sqlite3.connect('resultado_Miss_Marple.db')
cursor = conn.cursor()

# Se crean cinco tablas para almacenar proveedores, categorías, piezas y sus relaciones.

# Crear las tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS proveedor (
        idProveedor INTEGER PRIMARY KEY,
        nombre TEXT,
        direccion TEXT,
        ciudad TEXT,
        provincia TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS categoria (
        idCategoria INTEGER PRIMARY KEY,
        nombre TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pieza (
        idPieza INTEGER PRIMARY KEY,
        nombre TEXT,
        color TEXT,
        precio DECIMAL(10, 2)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pieza_categoria (
        idPieza INTEGER,
        idCategoria INTEGER,
        PRIMARY KEY (idPieza, idCategoria),
        FOREIGN KEY (idPieza) REFERENCES pieza(idPieza),
        FOREIGN KEY (idCategoria) REFERENCES categoria(idCategoria)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS suministro (
        idProveedor INTEGER,
        idPieza INTEGER,
        fecha DATE,
        cantidad INTEGER,
        PRIMARY KEY (idProveedor, idPieza, fecha),
        FOREIGN KEY (idProveedor) REFERENCES proveedor(idProveedor),
        FOREIGN KEY (idPieza) REFERENCES pieza(idPieza)
    )
""")

# Insertar datos representativos para simular el funcionamiento de la base de datos.


cursor.execute("INSERT INTO proveedor (idProveedor, nombre, direccion, ciudad, provincia) VALUES (?, ?, ?, ?, ?)", (1, 'Proveedor A', 'Calle Ficticia 123', 'Ciudad A', 'Provincia A'))
cursor.execute("INSERT INTO proveedor (idProveedor, nombre, direccion, ciudad, provincia) VALUES (?, ?, ?, ?, ?)", (2, 'Proveedor B', 'Avenida Falsa 456', 'Ciudad B', 'Provincia B'))

cursor.execute("INSERT INTO categoria (idCategoria, nombre) VALUES (?, ?)", (1, 'Electrónica'))
cursor.execute("INSERT INTO categoria (idCategoria, nombre) VALUES (?, ?)", (2, 'Mobiliario'))

cursor.execute("INSERT INTO pieza (idPieza, nombre, color, precio) VALUES (?, ?, ?, ?)", (1, 'Televisor', 'Negro', 299.99))
cursor.execute("INSERT INTO pieza (idPieza, nombre, color, precio) VALUES (?, ?, ?, ?)", (2, 'Silla', 'Madera', 89.99))

cursor.execute("INSERT INTO pieza_categoria (idPieza, idCategoria) VALUES (?, ?)", (1, 1))
cursor.execute("INSERT INTO pieza_categoria (idPieza, idCategoria) VALUES (?, ?)", (1, 2))

cursor.execute("INSERT INTO suministro (idProveedor, idPieza, fecha, cantidad) VALUES (?, ?, ?, ?)", (1, 1, '2024-12-01', 50))
cursor.execute("INSERT INTO suministro (idProveedor, idPieza, fecha, cantidad) VALUES (?, ?, ?, ?)", (2, 2, '2024-12-02', 30))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("BBDD creada y datos insertados correctamente al archivo resultado_Miss_Marple.db.")



