import pymongo

#Información necesaria para conectarnos a MongoDB
MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIME_OUT=1000 
MONGO_URL_CLOUD="mongodb+srv://user:password@cluster0.5ha6bub.mongodb.net/"
MONGO_BASEDATOS="sample_training"
MONGO_COLECCION="zips"
 
try:
    #Variable cliente que se va a conectar al cliente de Mongo
    cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    #Pedimos la información de conexión
    cliente.server_info()
    #Mostramos mensaje de conexión correcta
    #print("Conexion con mongo exitosa")
    db = cliente[MONGO_BASEDATOS]
    coleccion = db[MONGO_COLECCION]
    #Cerramos conexión
    #cliente.close()
    #Vamos a recoger los posibles errores que pudiéramos tener, en este caso, exceso de tiempo de respuesta
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    #Mostramos mensaje en tal caso
    print("Tiempo excedido de carga")
    #También recogemos el posible error de conexión
except pymongo.errors.ConnectionFailure as errorConexion:
    #Mostramos un mensaje en tal caso
    print("Fallo al conectarse a mongodb"+errorConexion)
