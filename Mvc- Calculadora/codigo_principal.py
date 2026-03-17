import tkinter as tk 

from modelo_calculadora import Calculadora
from vista import Vista
from controlador import Controlador

ventana = tk.Tk()

modelo_calc = Calculadora()

vista = Vista(ventana)

controlador = Controlador(modelo_calc, vista)

ventana.mainloop()