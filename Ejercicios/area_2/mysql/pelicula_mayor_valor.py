from conexion import conexion

cursor = conexion.cursor()
cursor.execute("""SELECT Titulo, Presupuesto
                FROM Peliculas
                ORDER BY 2 DESC
                LIMIT 1;""")
valor = cursor.fetchone()

print(f"La pelicula '{valor[0]}' tuvo el mayor presupuesto ({valor[1]}€)")
    
conexion.close()

