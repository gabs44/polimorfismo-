from FormaPlana import FormaPlana as C
import math

class Circulo(C):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio **2
    
    def perimetro(self):
        return 2 * math.pi * self.raio

    def descricao(self):
        return 'círculo'
