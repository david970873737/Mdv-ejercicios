import tkinter as tk 

class Vista:
    def __init__(self,ventana):
        self.ventana = ventana
        self.title = ("Calculadora")

        self.seccion1 = tk.Frame(ventana)


        tk.Label(self.seccion1,text="Ingresa el Usuario").grid(row=0,column=0)
        self.usu = tk.Entry(self.seccion1)
        self.usu.grid(row=0, column=1)
        tk.Label(self.seccion1, text="Ingresar el ID").grid(row=1, column=0)
        self.iden = tk.Entry(self.seccion1)
        self.iden.grid(row=1, column=1)

        self.resultado = tk.Label(self.seccion1, text="Info:")
        self.resultado.grid(row=2, column=0,columnspan=2)

        self.seccion2 = tk.Frame(ventana)

        tk.Label(self.seccion2, text= "Numero 1").grid(row=0, column= 0)
        self.num1 = tk.Entry(self.seccion2)
        self.num1.grid(row=0, column=1)
        tk.Label(self.seccion2, text= "Numero 2").grid(row=1, column=0)
        self.num2 = tk.Entry(self.seccion2)
        self.num2.grid(row=1, column=1)

        #botones

        self.btn_suma = tk.Button(self.seccion2, text= "+")
        self.btn_suma.grid(row=2, column=0 )

        self.btn_resta = tk.Button(self.seccion2, text= "-")
        self.btn_resta.grid(row=2, column=1 )

        self.btn_multiplicacion = tk.Button(self.seccion2, text= "*")
        self.btn_multiplicacion.grid(row=3, column=0 )

        self.btn_division = tk.Button(self.seccion2 , text= "/")
        self.btn_division.grid(row=3, column=1 )


        #resultado

        self.resultado = tk.Label(self.seccion2, text="Resultado:")
        self.resultado.grid(row=4, column=0,columnspan=2)

    def mostrar_resultado(self, valor):
        self.resultado.config(text=f"resultado: {valor}, {self.usu}, {self.iden} ")