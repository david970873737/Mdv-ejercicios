from modelo_numero import Numero     

class Controlador:
    def __init__(self,modelo_calc, vista):
        self.modelo_calc = modelo_calc
        self.vista = vista

        self.vista.btn_suma.config(command =self.sumar)
        self.vista.btn_resta.config(command =self.restar)
        self.vista.btn_multiplicacion.config(command =self.multiplicar)
        self.vista.btn_division.config(command =self.division)

    def obtener_valores(self):

        n1 = Numero(self.vista.num1.get())
        n2 = Numero(self.vista.num2.get())

        return n1.get_valor(), n2.get_valor()
    
    def sumar(self):
        a, b = self.obtener_valores()

        resultado = self.modelo_calc.sumar(a,b)

        self.vista.mostrar_resultado(resultado)
         

        
        