from conexion import conexion

cursor = conexion.cursor()
cursor.execute("SELECT Titulo FROM Peliculas;")

for elemento in cursor:
    print(elemento)
    
conexion.close()

