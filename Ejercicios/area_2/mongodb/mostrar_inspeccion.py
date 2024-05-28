from tkinter import*
from tkinter import ttk
from conexion import coleccion

def mostrarDatos(tabla):
    documentos = coleccion.find()
    for documento in documentos:
        tabla.insert('',
                    0,
                    text = documento["business_name"],
                    values = documento["certificate_number"])

ventana = Tk()
tabla = ttk.Treeview(ventana, columns = 2)
tabla.grid(row = 1, column = 0, columnspan = 2)
tabla.heading("#0", text = "BUSINESS_NAME")
tabla.heading("#1", text = "CERTIFICATE_NUMBER")
mostrarDatos(tabla)
ventana.mainloop()

