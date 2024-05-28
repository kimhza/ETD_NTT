from conexion import coleccion

documentos = coleccion.find({"city": "Madrid"})
print(f"Forma1: {list(documentos)}")

documentos = coleccion.find()
for doc in documentos:
    if doc["city"] == "Madrid":
        print(f"Forma2: {(doc)}")


