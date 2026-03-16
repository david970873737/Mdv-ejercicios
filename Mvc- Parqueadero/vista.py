import tkinter as tk

class Vista:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Parqueadero")

        tk.Label(ventana, text= "nombre").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(ventana)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(ventana, text= "id").grid(row=1, column=0)
        self.id_entry = tk.Entry(ventana)   
        self.id_entry.grid(row=1, column=1)

        tk.Label(ventana, text= "marca").grid(row=2, column=0)
        self.marca_entry = tk.Entry(ventana)
        self.marca_entry.grid(row=2, column=1)

        tk.Label(ventana, text= "placa").grid(row=3, column=0)
        self.placa_entry = tk.Entry(ventana)
        self.placa_entry.grid(row=3, column=1)

        tk.Label(ventana, text= "color").grid(row=4, column=0)
        self.color_entry = tk.Entry(ventana)
        self.color_entry.grid(row=4, column=1)

        tk.Label(ventana, text= "puesto").grid(row=5, column=0)
        self.puesto_entry = tk.Entry(ventana)
        self.puesto_entry.grid(row=5, column=1)

    #Botones 
        self.ingresar_button = tk.Button(ventana, text="Ingresar Carro")
        self.ingresar_button.grid(row=6, column=0)

        self.sacar_button = tk.Button(ventana, text="Sacar Carro")
        self.sacar_button.grid(row=6, column=1)


        #_-----------------

        self.texto_resultado = tk.Text(ventana, height=10, width=50)
        self.texto_resultado.grid(row=7, column=0, columnspan=2)

    def mostrar_resultado(self, mensaje):
        self.texto_resultado.insert(tk.END, mensaje + "\n")