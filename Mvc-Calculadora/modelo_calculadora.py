class Calculadora:
    def sumar(self, numero1, numero2):
        return numero1.get_valor() + numero2.get_valor()
    
    def restar(self, numero1, numero2):
        return numero1.get_valor() - numero2.get_valor()
    
    def multiplicar(self, numero1, numero2):
        return numero1.get_valor() * numero2.get_valor()
    
    def division(self, numero1, numero2):
        if numero2 == 0:
            return "ERROR no se puede dividir en 0 "
        else:
            return numero1.get_valor() / numero2.get_valor()
        