from conexion import conexion

cursor = conexion.cursor()
consulta = ('INSERT INTO Peliculas (ID, Titulo, Año, Presupuesto)'
            'VALUES (%s, %s, %s, %s);')
datos = [(1,"El padrino", 1972, 6000000),
         (2,"Tiburón", 1975, 9000000),
         (3,"Los cazafantasmas", 1984, 30000000),
         (4,"El exorcista", 1973, 12000000),
         (5,"Pulp Fiction", 1994, 8000000)]
cursor.executemany(consulta, datos)
conexion.commit()

if cursor:
    print("Datos insertados...")
cursor.execute("SELECT * FROM Peliculas;")
for elemento in cursor:
    print(elemento)
    
conexion.close()
