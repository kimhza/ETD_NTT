import mysql.connector

conexion = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='Cine',
    port='3307')


#if conexion:
#    print("Conectado")
