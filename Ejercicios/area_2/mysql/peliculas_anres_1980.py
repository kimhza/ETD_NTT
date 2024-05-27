from conexion import conexion

cursor = conexion.cursor()
cursor.execute("""SELECT * FROM Peliculas 
               WHERE Año < 1980;""")

for elemento in cursor:
    print(elemento)
    
conexion.close()

