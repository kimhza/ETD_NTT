from conexion import conexion

cursor = conexion.cursor()
cursor.execute("""SELECT * FROM Peliculas 
               WHERE Titulo like 'E%';""")

for elemento in cursor:
    print(elemento)
    
conexion.close()

