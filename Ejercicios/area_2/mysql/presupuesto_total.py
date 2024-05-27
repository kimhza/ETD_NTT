from conexion import conexion

cursor = conexion.cursor()
cursor.execute("""SELECT SUM(Presupuesto) AS Presupuesto 
                  FROM Peliculas;""")
valor = cursor.fetchone()

print(f"El presupuesto total empleado en las peliculas es {valor[0]}€")
    
conexion.close()

