from tkinter import*
from tkinter import ttk
from conexion import coleccion

def mostrarDatos(tabla):
    documentos = coleccion.find({"city": "BREMEN"})
    for documento in documentos:
        tabla.insert('',
                    0,
                    text = documento["zip"],
                    values = documento["pop"])

ventana = Tk()
tabla = ttk.Treeview(ventana, columns = 2)
tabla.grid(row = 1, column = 0, columnspan = 2)
tabla.heading("#0", text = "ZIP")
tabla.heading("#1", text = "POPULATION")
mostrarDatos(tabla)
ventana.mainloop()

