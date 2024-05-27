from conexion import conexion

cursor = conexion.cursor()
cursor.execute("""DELETE
                FROM Peliculas
                WHERE Año < 1980;""")
conexion.commit()

cursor.execute("""SELECT *
                FROM Peliculas""")
peliculas = cursor.fetchall()

print("Peliculas restantes: ")
for pelicula in peliculas:
    print(f"* {pelicula[1]} - Año: {pelicula[2]}")
    
conexion.close()

