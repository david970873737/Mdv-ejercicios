from datetime import datetime

class Parqueadero:
    def __init__(self):
        self.__puestos = {}

    def ingresar_carro(self, puesto, carro, usuario):
        self.__puestos[puesto] = {
            'carro': carro,
            'usuario': usuario,
            'hora_ingreso': datetime.now()
        }

    def sacar_carro(self, puesto):
        if puesto in self.__puestos:
            return self.__puestos.pop(puesto)
        return None