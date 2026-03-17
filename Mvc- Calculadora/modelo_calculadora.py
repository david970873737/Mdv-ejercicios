class Calculadora:

    def sumar(self, numero1, numero2):
        return numero1 + numero2

    def restar(self, numero1, numero2):
        return numero1 - numero2

    def multiplicar(self, numero1, numero2):
        return numero1 * numero2

    def division(self, numero1, numero2):
        if numero2 == 0:
            return "ERROR, no se puede dividir en cero"
        else:
            return numero1 / numero2