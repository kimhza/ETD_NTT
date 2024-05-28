from tkinter import*
from tkinter import ttk
from tkinter import messagebox 
import pymongo
 
#Información necesaria para conectarnos a MongoDB
MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIME_OUT=1000 #Por defecto necesita un time out para realizar la conexión
 
#Formamos la URL de conexión manualmente
MONGO_URL_LOCAL="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/" #Aquí puedes poner cualquier dirección. Esta dirección te conectará con el localhost (Compass). Al final del código explicaremos como
#Aquí puedes poner cualquier dirección. Esta dirección te conectará con el localhost (Compass). Al final del código explicaremos como conectar Compass con Atlas para poder trabajar con las bases de datos que creamos en la unidad MongoDB.
MONGO_URL_CLOUD="mongodb+srv://user:password@cluster0.5ha6bub.mongodb.net/"
 
#Declaramos dos variables para la base de datos y la colección con sus nombres
MONGO_BASEDATOS="sample_restaurants"
MONGO_COLECCION="Restaurants"
 
#Variable cliente que se va a conectar al cliente de Mongo
cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
baseDatos=cliente[MONGO_BASEDATOS]
coleccion=baseDatos[MONGO_COLECCION]

def mostrarDatos(tabla):
    try:
        for documento in coleccion.find():
            tabla.insert('',0,text=documento["name"],values=documento["cuisine"])
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb "+errorConexion)

ventana=Tk()
tabla=ttk.Treeview(ventana,columns=2)
tabla.grid(row=1,column=0,columnspan=2)
tabla.heading("#0",text="RESTAURANTE")
tabla.heading("#1",text="TIPO COCINA")
mostrarDatos(tabla)
#Mostramos la ventana
ventana.mainloop()
