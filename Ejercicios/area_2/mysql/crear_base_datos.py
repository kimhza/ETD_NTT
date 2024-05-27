from conexion import conexion

cursor = conexion.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Cine")
if cursor:
    print("Base de datos creada")
    
cursor.execute("SHOW DATABASES")
for base in cursor:
 print(base)

conexion.close()

