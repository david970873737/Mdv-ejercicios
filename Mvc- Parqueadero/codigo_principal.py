import tkinter as tk

from modelo_parqueadero import Parqueadero
from vista import Vista
from controlador import Controlador

ventana = tk.Tk()

modelo = Parqueadero()

vista = Vista(ventana)

controlador = Controlador(modelo, vista)#inyeccion de dependencias

ventana.mainloop()