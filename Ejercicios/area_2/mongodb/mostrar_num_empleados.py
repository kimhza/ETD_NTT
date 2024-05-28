from conexion import coleccion

documentos = coleccion.aggregate([
        {"$group": {
            "_id": None, 
            "empleados": {
                "$sum": "$number_of_employees"}
        }}
    ]
)

resultado = list(documentos)
empleados = resultado[0]["empleados"]

print(f"El número de empleados de todas las compañias es: {empleados}")


