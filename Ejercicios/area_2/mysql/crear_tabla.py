from conexion import conexion

cursor = conexion.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Peliculas'
                '(ID INT NOT NULL AUTO_INCREMENT,'
                'Titulo VARCHAR(45),'
                'Año INT(4),'
                'Presupuesto INT,'
                'PRIMARY KEY (ID));')
if cursor:
    print("Tabla creada")
    
cursor.execute('DESCRIBE Peliculas')
for base in cursor:
 print(base)

conexion.close()
