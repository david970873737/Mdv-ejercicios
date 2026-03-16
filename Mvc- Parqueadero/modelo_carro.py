class Carro:
    def __init__(self, marca, placa, color):
        self.marca = marca
        self.placa = placa
        self.color = color

    def get_marca(self):
        return self.marca

    def get_placa(self):
        return self.placa
    
    def get_color(self):
        return self.color
    
    def set_marca(self, marca):
        self.marca = marca

    def set_placa(self, placa):
        self.placa = placa

    def set_color(self, color):
        self.color = color

    def validar_carro(self):
        if self.marca and self.placa and self.color:
            return True
        return False