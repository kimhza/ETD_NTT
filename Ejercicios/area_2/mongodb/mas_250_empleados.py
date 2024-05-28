from conexion import coleccion

documentos = coleccion.find({
    "number_of_employees": 
        {
            "$gt": 250
        }
})

for doc in documentos:
    print(f"Compañia: {doc['name']} | Empleados: {doc['number_of_employees']}")


