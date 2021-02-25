from FormaPlana import FormaPlana as R
import math 

class Retangulo(R):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    
    def area(self):
        return self.lado1 * self.lado2

    def perimetro(self):
        return self.lado1 * 2 + self.lado2 * 2

    def diagonal(self):
        return math.sqrt(self.lado1 **2 + self.lado2 **2)

    def descricao(self):
        return 'retângulo '


