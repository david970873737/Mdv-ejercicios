from modelo_usuario import Usuario
from modelo_carro import Carro

class Controlador:
    def __init__(self, modelo, vista):  # inyección de dependencias
        self.modelo = modelo
        self.vista = vista

        # botones de la vista con funciones del controlador
        self.vista.ingresar_button.config(command=self.ingresar_carro)
        self.vista.sacar_button.config(command=self.sacar_carro)

    def ingresar_carro(self):
        nombre = self.vista.nombre_entry.get()
        id_usuario = self.vista.id_entry.get()
        marca = self.vista.marca_entry.get()
        placa = self.vista.placa_entry.get()
        color = self.vista.color_entry.get()
        puesto = self.vista.puesto_entry.get()

        usuario = Usuario(nombre, id_usuario)
        carro = Carro(marca, placa, color)

        # validación de datos antes de ingresar el carro al parqueadero
        if usuario.validar_usuario() and carro.validar_carro():
            self.modelo.ingresar_carro(puesto, carro, usuario)
            self.vista.mostrar_resultado(f"Carro ingresado en el puesto {puesto}")
        else:
            self.vista.mostrar_resultado("Datos inválidos para el usuario o el carro")

    def sacar_carro(self):
        puesto = self.vista.puesto_entry.get()
        resultado = self.modelo.sacar_carro(puesto)

        if resultado:
            carro = resultado['carro']
            usuario = resultado['usuario']
            hora_ingreso = resultado['hora_ingreso']

            self.vista.mostrar_resultado(
                f"Carro {carro.get_marca()} con placa {carro.get_placa()} "
                f"sacado por {usuario.get_nombre()} a las {hora_ingreso}"
            )
        else:
            self.vista.mostrar_resultado("No hay carro en ese puesto")