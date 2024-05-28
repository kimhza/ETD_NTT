from conexion import coleccion

insertar_documento = coleccion.insert_one({
    "city": "Madrid",
    "zip": "458971",
    "loc": (40.342553, -3.171997),
    "pop": 11111,
    "state": "SP"
})

id = insertar_documento.inserted_id

documento = coleccion.find({"_id": id})
print(list(documento))

