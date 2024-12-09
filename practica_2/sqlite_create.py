import sqlite3

# Conexión a SQLite
conn = sqlite3.connect('resultado_miss_marple.db')
cursor = conn.cursor()

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

# Insertar datos representativos en proveedor
proveedores = [
    (1, 'Proveedor A', 'Calle Ficticia 123', 'Ciudad A', 'Provincia A'),
    (2, 'Proveedor B', 'Avenida Falsa 456', 'Ciudad B', 'Provincia B'),
    (3, 'Proveedor C', 'Camino Imaginario 789', 'Ciudad C', 'Provincia C'),
    (4, 'Proveedor D', 'Plaza Inventada 321', 'Ciudad D', 'Provincia D'),
    (5, 'Proveedor E', 'Boulevard Fantasía 654', 'Ciudad E', 'Provincia E')
]
cursor.executemany("INSERT INTO proveedor (idProveedor, nombre, direccion, ciudad, provincia) VALUES (?, ?, ?, ?, ?)", proveedores)

# Insertar datos representativos en categoria
categorias = [
    (1, 'Electrónica'),
    (2, 'Mobiliario'),
    (3, 'Automoción'),
    (4, 'Juguetes'),
    (5, 'Hogar')
]
cursor.executemany("INSERT INTO categoria (idCategoria, nombre) VALUES (?, ?)", categorias)

# Insertar datos representativos en pieza
piezas = [
    (1, 'Televisor', 'Negro', 299.99),
    (2, 'Silla', 'Madera', 89.99),
    (3, 'Mesa', 'Blanco', 149.99),
    (4, 'Ordenador', 'Gris', 899.99),
    (5, 'Coche de juguete', 'Rojo', 19.99),
    (6, 'Sofá', 'Azul', 499.99),
    (7, 'Refrigerador', 'Plateado', 749.99),
    (8, 'Lámpara', 'Amarillo', 29.99),
    (9, 'Lavadora', 'Blanco', 399.99),
    (10, 'Auriculares', 'Negro', 59.99)
]
cursor.executemany("INSERT INTO pieza (idPieza, nombre, color, precio) VALUES (?, ?, ?, ?)", piezas)

# Insertar relaciones en pieza_categoria
pieza_categoria = [
    (1, 1),
    (2, 2),
    (3, 2),
    (4, 1),
    (5, 4),
    (6, 2),
    (7, 5),
    (8, 5),
    (9, 5),
    (10, 1)
]
cursor.executemany("INSERT INTO pieza_categoria (idPieza, idCategoria) VALUES (?, ?)", pieza_categoria)

# Insertar datos representativos en suministro
suministros = [
    (1, 1, '2024-12-01', 50),
    (2, 2, '2024-12-02', 30),
    (3, 3, '2024-12-03', 20),
    (4, 4, '2024-12-04', 10),
    (5, 5, '2024-12-05', 100),
    (1, 6, '2024-12-06', 15),
    (2, 7, '2024-12-07', 25),
    (3, 8, '2024-12-08', 40),
    (4, 9, '2024-12-09', 60),
    (5, 10, '2024-12-10', 70)
]
cursor.executemany("INSERT INTO suministro (idProveedor, idPieza, fecha, cantidad) VALUES (?, ?, ?, ?)", suministros)

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("BBDD creada y datos insertados correctamente al archivo resultado_miss_marple.db.")
