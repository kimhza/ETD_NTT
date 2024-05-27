from conexion import conexion

cursor = conexion.cursor()
cursor.execute("""SELECT Titulo
                FROM Peliculas
                ORDER BY 1;""")
peliculas = cursor.fetchall()

print("Nombres de peliculas ordenados alfabeticamente: ")
for pelicula in peliculas:
    print(f"* {pelicula[0]}")
    
conexion.close()

